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
