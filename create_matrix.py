import json

# Your specific environment parameters
MY_PYTHON_VERSION = ["3.12"]
MY_TORCH_VERSION = ["2.9.1"]
MY_CUDA_VERSION = ["12.8"]
MY_FLASH_ATTN_VERSION = ["2.8.3"]

# The EXCLUDE list is kept as-is for reference
EXCLUDE = [
    {"python-version": "3.12", "torch-version": "2.0.1"},
    {"python-version": "3.12", "torch-version": "2.1.2"},
    {"torch-version": "2.0.1", "cuda-version": "12.1"},
    {"torch-version": "2.0.1", "cuda-version": "12.4"},
    {"torch-version": "2.0.1", "cuda-version": "12.6"},
    {"torch-version": "2.0.1", "cuda-version": "12.8"},
    {"torch-version": "2.6.0", "cuda-version": "12.1"},
    {"torch-version": "2.7.0", "cuda-version": "12.4"},
    {"torch-version": "2.5.1", "cuda-version": "12.9"},
    {"torch-version": "2.6.3", "cuda-version": "12.9"},
    {"torch-version": "2.7.1", "cuda-version": "12.9"},
    {"torch-version": "2.9.1", "python-version": "3.9"},
    {"torch-version": "2.5.1", "cuda-version": "13.0"},
    {"torch-version": "2.6.0", "cuda-version": "13.0"},
    {"torch-version": "2.7.1", "cuda-version": "13.0"},
    {"torch-version": "2.8.1", "cuda-version": "13.0"},
    {"torch-version": "2.8.0", "cuda-version": "13.0"},
    {"torch-version": "2.5.1", "python-version": "3.14"},
    {"torch-version": "2.6.3", "python-version": "3.14"},
    {"torch-version": "2.7.1", "python-version": "3.14"},
    {"torch-version": "2.8.0", "python-version": "3.14"},
]

# Disable all Linux matrices
LINUX_MATRIX = False
LINUX_ARM64_MATRIX = False
LINUX_SELF_HOSTED_MATRIX = False
LINUX_ARM64_SELF_HOSTED_MATRIX = False
WINDOWS_CODEBUILD_MATRIX = False

# Only this Windows matrix will run
WINDOWS_MATRIX = {
    "flash-attn-version": MY_FLASH_ATTN_VERSION,
    "python-version": MY_PYTHON_VERSION,
    "torch-version": MY_TORCH_VERSION,
    "cuda-version": MY_CUDA_VERSION,
}

def main():
    print(
        json.dumps(
            {
                "linux": LINUX_MATRIX,
                "linux_arm64": LINUX_ARM64_MATRIX,
                "linux_self_hosted": LINUX_SELF_HOSTED_MATRIX,
                "linux_arm64_self_hosted": LINUX_ARM64_SELF_HOSTED_MATRIX,
                "windows": WINDOWS_MATRIX,
                "windows_code_build": WINDOWS_CODEBUILD_MATRIX,
                "exclude": EXCLUDE,
            }
        )
    )

if __name__ == "__main__":
    main()
