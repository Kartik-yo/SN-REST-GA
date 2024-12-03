import sys

def build_application():
    print("Starting build process...")
    # Simulate build failure for testing
    raise Exception("Simulated Build Failure")

if __name__ == "__main__":
    try:
        build_application()
    except Exception as error:
        print(f"Build failed: {error}")
        sys.exit(1)
