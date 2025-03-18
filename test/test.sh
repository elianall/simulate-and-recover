#!/bin/bash
# test/test.sh
# Run the unit tests for the EZ diffusion module.

echo "Running unit tests for EZDiffusion..."
python3 -m unittest discover -s test
if [ $? -eq 0 ]; then
    echo "All unit tests passed successfully."
else
    echo "Some unit tests failed."
    exit 1
fi

chmod +x test/test.sh
