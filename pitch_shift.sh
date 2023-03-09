#!/bin/bash

# Generated with the help of ChatGPT

# Create the results directory if it doesn't exist
mkdir -p results

# Loop through all WAV files in the current directory
for file in *.wav; do
    # Create the output file name in the results directory
    output_file="results/$(basename "$file")"

    # Use sox to pitch shift the WAV file by one semitone
    sox "$file" "$output_file" pitch 100

    echo "Pitch shifted $file to $output_file"
done
