################################
## hw0: Anita Slater
## Data Mining/ Machine Learning
################################

## 1: 
def test_print():
	print("This is a test statement.")
if __name__=='__main__':
	test_print()

## 2:
def list_set_length(items_list,items_set):
	items_list = [1,2,3,4,3,2,1]
	items_set={1,2,3,4,3,2,1}

	print("The list contains",len(items_list), "items")
	print("The set  contains",len(items_set), "items")

test_list=[]
test_set={}

list_set_length(test_list,test_set)

## 3:
def set_intersect(S,T):
	return {x+0 for x in S for y in T if x==y}
		
print(set_intersect({1,2,3,4},{3,4,5,6}))		

## 4:
def three_tuples(S):
	return [ (i,j,k) for i in S for j in S for k in S if i+j+k==0]

print(three_tuples({-4,-2,1,2,5,0}))

