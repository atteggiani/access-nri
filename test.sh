#!/bin/bash
str="$1"
regex="$2"

function my_grep() {
    perl_script=$(cat << EOF
if ( "$1" =~ /($2)/) {
    print "\$1\n";
}
EOF
)    
    perl -e "$perl_script"
}

my_grep "$str" "$regex"

grep -Po $regex <<< "$str"