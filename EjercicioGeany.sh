path=$(pwd) 
A=1
B=0
for i in $(seq 1 1 10)
do
C=$(($A + $B))
A=$B
B=$C
path="$path/$C"
mkdir $path
done
ls / -la>$path/root.txt
ls ~ -la>$path/home.txt
echo "Jimmy Alejandro Bonilla Rincón">$path/Nombre_estudiante.txt
