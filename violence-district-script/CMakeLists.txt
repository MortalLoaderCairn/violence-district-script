cmake_minimum_required(VERSION 3.10)
project(ViolenceDistrictScript)

set(CMAKE_CXX_STANDARD 17)

add_executable(violence_district_script src/main.cpp src/roblox_utils.cpp src/script_hooks.cpp)
target_include_directories(violence_district_script PRIVATE include)