cd ~

delete_files() {
  for file in $(ls)
  do
    if [ -d $file ]
    then
      cd $file
      delete_files
      cd ..
    else
      case $(file -0 "$file" | cut -d $'\0' -f2) in
        (*text*)
        (*)
          rm -f $file
      esac
    fi
  done
}

delete_files
