leaf=2
for num in 1 2 3
do
	echo "Run for repeat ${num}:"
	python Commands/rootF1Global.py input/original/test.txt input/logistic/logistic_leaf${leaf}_re${num}_test.txt
	echo "\n"
done