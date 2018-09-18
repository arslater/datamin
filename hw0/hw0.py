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


## 5:
def dict_init():
	## 5a:
	mydict = {'Neo':'Keanu', 'Morpheus':'Laurence', 'Trinity':'Carrie-Anne'}
	return mydict
def dict_find(dlist, k):
	return {dlist[i] for i in dlist if dlist[i].get(k) == k}
print (dict_find([('cat':'fluffy','dog':'fido','fish':'swimmy')],[('pizza':'italian'),('toast':'french')],'pizza'))


def dict_find(dlist, k):
	print([d, for d in dlist for val in d if val==k else 'NOT PRESENT'] )
pet_dict  = {'cat':'fluffy','dog':'fido','fish':'swimmy'}
food_dict = {'pizza':'italian','toast':'french'}
mast_dict = []
mast_dict.append(pet_dict)
mast_dict.append(food_dict)

# print(dict_find(mast_dict,'cat'))
#print(mast_dict)
dict_find(mast_dict,'cat')