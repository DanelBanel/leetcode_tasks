#!/bin/bash

# Define folders and their corresponding file endings
declare -A folders
folders=( ["python"]=".py" ["cpp"]=".hpp .cpp" ["javascript"]=".js" )

# Function to check file endings
check_file_endings() {
    local folder=$1
    local endings=$2
    local valid=0

    for file in "$folder"/*; do
        if [ -f "$file" ]; then
            local extension="${file##*.}"
            if [[ ! " $endings " =~ " .$extension " ]]; then
                echo "Invalid file ending: $file"
                valid=1
            fi
        fi
    done

    return $valid
}

# Iterate over folders and check file endings
for folder in "${!folders[@]}"; do
    if [ -d "$folder" ]; then
        echo "Checking folder: $folder"
        check_file_endings "$folder" "${folders[$folder]}"
        if [ $? -eq 0 ]; then
            echo "All files in $folder have valid endings."
        else
            echo "Some files in $folder have invalid endings."
        fi
    else
        echo "Folder $folder does not exist."
    fi
done