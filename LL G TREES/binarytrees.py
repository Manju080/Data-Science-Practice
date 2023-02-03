class BinarySearchTree:
    def __init__(self,data):
        self.data =data
        self.left=None
        self.right=None
    def add_child(self,data):
        if data==self.data:
            return 
        if data<self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left=BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right=BinarySearchTree(data)
    def in_order_traverse(self):
        elements=[]
        if self.left:
            elements+=self.left.in_order_traverse()
        elements.append(self.data)
        if self.right:
            elements+=self.right.in_order_traverse()
        return elements
    def search(self,val):
        if self.data==val:
            return True
        if val<self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
        if val>self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    def max_val(self):
        if self.right is None:
            return self.data  
        return self.right.max_val() 
    def min_val(self):
        if self.left is None:
            return self.data
        return self.left.min_val()
    def calculate_sum(self):
        left_sum=self.left.calculate_sum() if self.left else 0
        right_sum=self.right.calculate_sum() if self.right else 0
        return self.data+left_sum+right_sum
    def pre_order(self):
        elements=[self.data]
        root=BinarySearchTree(self.data)
        if self.left:
            elements+=self.left.pre_order()
        if self.right:
            elements +=self.right.pre_order()
        return elements 
    def post_order(self):
        elements=[]
        if self.left:
            elements += self.left.post_order()
        if self.right:
            elements += self.right.post_order()
        elements.append(self.data)
        return elements

    def Delete(self,val):
        if val<self.data:
            if self.left:
                self.left.Delete(val)
        elif val>self.data:
            if self.right:
                self.right.Delete(val)
        else:
            if self.right is None and self.left is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.right

            mini=self.right.max_val()
            self.data=mini
            self.left=self.left.Delete(mini)
        return self
            
            
def build_tree(elements):
    root=BinarySearchTree(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root

if __name__== '__main__':
    numbers=[17,4,1,20,9,23,18,34]
    numbers_tree= build_tree(numbers)
    # print(numbers_tree.max_val())
    # print(numbers_tree.min_val())
    # print(numbers_tree.calculate_sum())
    # print(numbers_tree.post_order())
    print(numbers_tree.pre_order())
    print(numbers_tree.Delete(20))
    print(numbers_tree.in_order_traverse())