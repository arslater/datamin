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
	return [['NOT PRESENT',d][val==k] for d in dlist for val in d ]

## 6
def file_line_count(infile):
	return(sum(1 for line in open(infile)))
print(file_line_count('stories.txt'))

## 7a
def make_inverse_index(strlist):
	document = [document for document in strlist]
	
	myDict={}	

	for i, value in enumerate(document,0):
		for word in value.split():
			if word in myDict:
				myDict[word].append(i)
			else:
				myDict.update({ word:[i]})

	return(myDict)

with open('stories.txt') as infile:
	document=infile.readlines()
document=[i.strip('\n') for i in document]

## 7b
def or_search(inverseIndex,query):	
	return([inverseIndex[item] for item in query if item in inverseIndex.keys()])

## 7c
def and_search(inverseIndex, query):
	andDict= []
	for item in query:
		if item not in inverseIndex.keys():
			return '[[]]'
	andDict.append(inverseIndex[item])
	return andDict                                                             

## 7d
with open("results.txt","a") as outfile:
	outfile.write(str(or_search(make_inverse_index(document),"united states" )))
	outfile.write(str(and_search(make_inverse_index(document),"united states" )))
	outfile.write(str(or_search(make_inverse_index(document),"wall street" )))
	outfile.write(str(and_search(make_inverse_index(document),"wall street" )))
