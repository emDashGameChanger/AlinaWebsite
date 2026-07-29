#!/bin/bash
# Reproducible setup for the BioLab docking toolchain: fpocket, the `biolab`
# conda env (PyMOL + Open Babel), and AutoDock-Vina-GPU-2.1 built from source.
# Mirrors the steps documented in molecularDocking/softwareInstall.html.
set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

FORCE=false
if [[ "$1" == "--force" ]]; then
  FORCE=true
fi

if [[ -f "./AutoDock-Vina-GPU-2-1" && "$FORCE" != "true" ]]; then
  echo "AutoDock-Vina-GPU-2-1 already present in biolab/. Nothing to do."
  echo "Re-run with --force to rebuild from scratch."
  exit 0
fi

# Protect PATH, per softwareInstall.html — some installs can trash it.
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

echo "==> Installing apt prerequisites (will prompt for sudo password)"
sudo apt update
sudo apt install -y build-essential git cmake libboost-all-dev libnetcdf-dev nvidia-cuda-toolkit

mkdir -p vendor
cd vendor

if [[ ! -d fpocket ]]; then
  echo "==> Cloning and building fpocket"
  git clone https://github.com/Discngine/fpocket.git
  (cd fpocket && make && sudo make install)
else
  echo "==> fpocket already present in vendor/, skipping"
fi

echo "==> Setting up conda env 'biolab' (pymol-open-source, openbabel)"
if conda env list | grep -q '^biolab '; then
  echo "conda env 'biolab' already exists, skipping creation"
else
  conda env create -f "$SCRIPT_DIR/environment.yml"
fi

if [[ ! -d Vina-GPU-2.1 ]]; then
  echo "==> Cloning AutoDock-Vina-GPU-2.1"
  git clone https://github.com/DeltaGroupNJUPT/Vina-GPU-2.1.git
else
  echo "==> Vina-GPU-2.1 already present in vendor/, skipping clone"
fi

cd Vina-GPU-2.1/AutoDock-Vina-GPU-2.1

export OPENCL_LIB_PATH=/usr/lib/x86_64-linux-gnu
export OPENCL_INC_PATH=/usr/include

echo "==> Initial one-shot build (kernel built from source)"
g++ -o AutoDock-Vina-GPU-2-1 \
  -I./lib -I./OpenCL/inc -I./main \
  -I/usr/include \
  ./main/main.cpp ./lib/*.cpp ./OpenCL/src/wrapcl.cpp \
  -O3 \
  -lboost_program_options -lboost_system -lboost_filesystem -lboost_thread -lOpenCL -lpthread -lstdc++fs \
  -DOPENCL_2_0 -DNVIDIA_PLATFORM -DSMALL_BOX -DNDEBUG -DBUILD_KERNEL_FROM_SOURCE \
  -DBOOST_TIMER_ENABLE_DEPRECATED

echo "==> Writing Makefile for rebuild"
cat > Makefile <<'MAKEFILE_EOF'
# 1. Path setup - using relative paths to avoid "shidi" errors
BOOST_LIB_PATH = /usr/lib/x86_64-linux-gnu
OPENCL_LIB_PATH = /usr/local/cuda

# 2. Include paths (The -I flags)
BOOST_INC_PATH = -I/usr/include
VINA_GPU_INC_PATH = -I./lib -I./OpenCL/inc
OPENCL_INC_PATH = -I$(OPENCL_LIB_PATH)/include

# 3. Library paths and flags (The -L and -l flags)
LIB_PATH = -L$(BOOST_LIB_PATH) -L$(OPENCL_LIB_PATH)/lib64
LIB_FLAGS = -lboost_program_options -lboost_thread -lboost_system -lboost_filesystem -lboost_timer -lOpenCL -lstdc++ -lstdc++fs -lm -lpthread

# 4. Source files
# Removed the problematic /libs/thread/src/pthread/ paths
SRC = ./lib/*.cpp ./OpenCL/src/wrapcl.cpp

# 5. Compiler settings
GPU_PLATFORM = -DNVIDIA_PLATFORM
OPENCL_VERSION = -DOPENCL_3_0
DOCKING_BOX_SIZE = -DSMALL_BOX
MACRO = $(OPENCL_VERSION) $(GPU_PLATFORM) $(DOCKING_BOX_SIZE) -DBOOST_TIMER_ENABLE_DEPRECATED

all: out

out: ./main/main.cpp
	gcc -o AutoDock-Vina-GPU-2-1 $(BOOST_INC_PATH) $(VINA_GPU_INC_PATH) $(OPENCL_INC_PATH) ./main/main.cpp -O3 $(SRC) $(LIB_FLAGS) $(LIB_PATH) $(MACRO) -DNDEBUG

source: ./main/main.cpp
	gcc -o AutoDock-Vina-GPU-2-1 $(BOOST_INC_PATH) $(VINA_GPU_INC_PATH) $(OPENCL_INC_PATH) ./main/main.cpp -O3 $(SRC) $(LIB_FLAGS) $(LIB_PATH) $(MACRO) -DNDEBUG -DBUILD_KERNEL_FROM_SOURCE

clean:
	rm -f AutoDock-Vina-GPU-2-1
MAKEFILE_EOF

echo "==> Patching OpenCL/src/wrapcl.cpp include"
sed -i 's/#include <wrapcl.h>/#include "wrapcl.h"/' OpenCL/src/wrapcl.cpp

make clean
make source

echo "==> Copying binary and linking OpenCL dir back into biolab/"
cp AutoDock-Vina-GPU-2-1 "$SCRIPT_DIR/"
ln -sf "$(pwd)/OpenCL" "$SCRIPT_DIR/OpenCL"

echo ""
echo "Setup complete."
echo "Note: Kernel1_Opt.bin / Kernel2_Opt.bin are OpenCL kernel caches generated"
echo "automatically the first time the binary runs on the GPU — no action needed."
echo ""
echo "Test with:"
echo "  cd $SCRIPT_DIR && conda activate biolab && ./AutoDock-Vina-GPU-2-1 --config config.txt"
