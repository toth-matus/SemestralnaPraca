import mmh3
import tkinter as tk
from tkinter import ttk

class BasicWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Student Database")
        self.root.configure(bg= "#303030")
        self.root.resizable(False, False)
        self.root.geometry(f"+{0}+{0}")
        
        self.Label_Name = tk.Label(self.root, text="Name", width=20, bg="#606060", )
        self.Label_SurName = tk.Label(self.root, text="Surname", width=20, bg="#606060", )
        self.Label_Number = tk.Label(self.root, text="Number", width=20, bg="#606060", )
        self.Label_Email = tk.Label(self.root, text="E-mail", width=20, bg="#606060",)

        self.Label_Name_Found = tk.Label(self.root, text="Name", width=12, bg="#404040",)
        self.Label_SurName_Found = tk.Label(self.root, text="Surname", width=12, bg="#404040",)
        self.Label_Number_Found = tk.Label(self.root, text="Number", width=20, bg="#404040",)
        self.Label_Email_Found = tk.Label(self.root, text="E-mail", width=20, bg="#404040",)
        
        self.Label_PlaceHolder1 = tk.Label(self.root, text="", width=20, height=1, bg="#303030",)
        self.Label_PlaceHolder2 = tk.Label(self.root, text="", width=20, height=2, bg="#303030",)
        self.Label_PlaceHolder3 = tk.Label(self.root, text="", width=20, height=1, bg="#303030",)
        self.Label_PlaceHolder4 = tk.Label(self.root, text="", width=20, height=2, bg="#303030",)
        
        self.Label_ErrorNoneFound = tk.Label(self.root, text="Error: No Student Found", width=62, height=1, bg="#606060", padx=7)
        self.Label_StudentAdded = tk.Label(self.root, text="Student Added To Database", width=62, height=1, bg="#606060", padx=7)
        self.Label_StudentRemoved = tk.Label(self.root, text="Student Removed From Database", width=62, height=1, bg="#606060", padx=7)
        self.Label_StudentsSameName = tk.Label(self.root, text="Multiple Dtudents With Same Name, Chose One To Delete", width=70, height=1, bg="#606060", padx=7)
        self.Label_ErrorEmptyEntry = tk.Label(self.root, text="Error: Empty Entry", width=70, height=1, bg="#606060", padx=7)

        self.Entry_Name = tk.Entry(self.root, width=40, bg="#606060")
        self.Entry_SurName = tk.Entry(self.root, width=40, bg="#606060")
        self.Entry_Number = tk.Entry(self.root, width=40, bg="#606060")
        self.Entry_Email = tk.Entry(self.root, width=40, bg="#606060")
        
        self.buttonAction_Add = tk.Button(self.root, text="Add!", width=38, command=self.AddData)
        self.buttonAction_Del = tk.Button(self.root, text="Delete!", width=38, command=self.DelData)
        self.buttonAction_Fin = tk.Button(self.root, text="Find!", width=38, command=self.FindData)
        
        self.buttonAdd_Black = ttk.Button(self.root, text="Add Student Data", width = 17, command=self.OpenAddWindow)
        self.buttonDel_Black = ttk.Button(self.root, text="Delete Student Data", width = 16, command=self.OpenDelWindow)
        self.buttonFin_Black = ttk.Button(self.root, text="Get Student Data", width = 16, command=self.OpenFinWindow)
        self.buttonBac = ttk.Button(self.root, text="Go back", width = 16, command=self.OpenAddWindow)
        
        self.buttonAdd_White = tk.Button(self.root, text="Add Student Data", width = 17,)
        self.buttonDel_White = tk.Button(self.root, text="Delete Student Data", width = 16,)
        self.buttonFin_White = tk.Button(self.root, text="Get Student Data", width = 16,)
        self.buttonDel = tk.Button(self.root, text="Delete!", width = 16,)


        
    def AddData(self):
        # Creating index and data list for new node
        self.data = []
        self.name = self.Entry_Name.get()
        self.data.append(self.name)
        self.surname = self.Entry_SurName.get()
        self.data.append(self.surname)
        self.number = self.Entry_Number.get()
        self.number.replace(" ","")
        self.data.append(self.number)
        self.email = self.Entry_Email.get()
        self.email.replace(" ","")
        self.data.append(self.email)
        self.name = self.name+self.surname
        
        if self.name == "" or self.surname == "" or self.email == "" or self.number == "":
            # Not accepting empty entries
            self.root.destroy()
            x = ErrorEmptyEntry()
        else:
            # Creating new node
            self.index = encode(self.name)
            database.add(self.index, self.data)
            self.root.destroy()
            x = StudentAdded()

    
    def FindData(self):
        self.name = self.Entry_Name.get()
        self.surname = self.Entry_SurName.get()
        self.name = self.name+self.surname
        if self.name == "" or self.surname == "": 
            # Not accepting empty entries
            self.root.destroy()
            x = ErrorEmptyEntry()
        else:
            # Finding node an either returning the data or error message
            self.index = encode(self.name)
            self.node = database.find(self.index)
            if self.node is None:
                self.root.destroy()
                x = ErrorNoneFound()
            else:
                self.root.destroy()
                x = FinData(self.node.data)

    def DelData(self):
        self.name = self.Entry_Name.get()
        self.surname = self.Entry_SurName.get()
        self.name = self.name+self.surname
        if self.name == "" or self.surname == "": 
            # Not accepting empty entries
            self.root.destroy()
            x = ErrorEmptyEntry()
        else:
            # Finding node an either deleting the data or error message
            index = encode(self.name)
            node = database.find(index)
            if node is None:
                self.root.destroy()
                x = ErrorNoneFound()
            elif len(node.data)>1:
                self.root.destroy()
                x = DelData(node, self.data)
            else:
                database.delete(node)
                self.root.destroy()
                x = StudentDeleted()

    def ChangeData(self, node, i):
        # Deleting one's data if more people have the same name
        data = node.data
        del data[i]
        node.data = data
        self.root.destroy()
        x=StudentDeleted()

    def OpenAddWindow(self):
        self.root.destroy()
        x = AddWindow()
        
    def OpenDelWindow(self):
        self.root.destroy()
        x = DelWindow()
        
    def OpenFinWindow(self):
        self.root.destroy()
        x = FinWindow()

class InputWindow():
    # Parent window to all input/entry windows
    def __init__(self):
        self.root = BasicWindow()
        self.root.Label_Name.grid(row=0, column=0, padx=5)
        self.root.Label_SurName.grid(row=1, column=0, padx=5)

        self.root.Entry_Name.grid(row=0, column=1, columnspan=2)
        self.root.Entry_SurName.grid(row=1, column=1, columnspan=2)

        self.root.buttonAdd_Black.grid(row=5, column=0,)
        self.root.buttonDel_Black.grid(row=5, column=1,)
        self.root.buttonFin_Black.grid(row=5, column=2,)
class AddWindow():
    # Window for adding data
    def __init__(self): 
        self.r = InputWindow()
        self.r.root.Label_Number.grid(row=2, column=0, padx=5)
        self.r.root.Label_Email.grid(row=3, column=0, padx=5)
        self.r.root.Entry_Number.grid(row=2, column=1, columnspan=2)
        self.r.root.Entry_Email.grid(row=3, column=1, columnspan=2) 
        self.r.root.buttonAction_Add.grid(row=4, column=1, columnspan=2,)
        self.r.root.buttonAdd_Black.destroy()
        self.r.root.buttonAdd_White.grid(row=5, column=0,)
        tk.mainloop()
class DelWindow():
    # Window for deleting data
    def __init__(self):
        self.r = InputWindow()
        self.r.root.buttonAction_Del.grid(row=2, column=1, columnspan=2)
        self.r.root.Label_PlaceHolder1.grid(row=3, column=0)
        self.r.root.Label_PlaceHolder2.grid(row=4, column=0)
        self.r.root.buttonDel_Black.destroy()
        self.r.root.buttonDel_White.grid(row=5, column=1,)
        tk.mainloop()
class FinWindow():
    # Window for finding data
    def __init__(self):
        self.r = InputWindow()
        self.r.root.buttonAction_Fin.grid(row=2, column=1, columnspan=2)
        self.r.root.Label_PlaceHolder1.grid(row=3, column=0)
        self.r.root.Label_PlaceHolder2.grid(row=4, column=0)
        self.r.root.buttonFin_Black.destroy()
        self.r.root.buttonFin_White.grid(row=5, column=2,)
        tk.mainloop()
    
class BasicData():
    # Window for showing data
    def __init__(self, data):
        self.root = BasicWindow()
        self.root.Label_Name_Found.grid(row=0, column=0, padx=2, pady=2)
        self.root.Label_SurName_Found.grid(row=0, column=1, padx=2)
        self.root.Label_Number_Found.grid(row=0, column=2, padx=2)
        self.root.Label_Email_Found.grid(row=0, column=3, padx=2)

        for i in range(len(data)):
            tk.Label(text=f"{data[i][0]}", width=12, bg="#606060", ).grid(row=i+1, column=0, pady=2 )
            tk.Label(text=f"{data[i][1]}", width=12, bg="#606060", ).grid(row=i+1, column=1, pady=2 )
            tk.Label(text=f"{data[i][2]}", width=20, bg="#606060", ).grid(row=i+1, column=2, pady=2 )
            tk.Label(text=f"{data[i][3]}", width=20, bg="#606060", ).grid(row=i+1, column=3, pady=2 )       
class FinData():
    # Window for showing found data
    def __init__(self,data) -> None:
        r=BasicData(data)
        r.root.buttonBac.grid(row=5, column=0, padx=2, columnspan=4)
        tk.mainloop()
class DelData():
    # Window for showing data to be deleted
    def __init__(self, node, data) -> None:
        self.r=BasicData(data)
        for i in range(len(data)):
            tk.Button(text="Delete!", width=2, command=lambda i=i:self.r.root.ChangeData(node,i)).grid(row=1+i, column=4)
        self.r.root.Label_StudentsSameName.grid(row=1000, columnspan=5)
        tk.mainloop()

class ResolutionWindow():
    # Window for showing error/resolution messages
    def __init__(self):
        self.root = BasicWindow()
        self.root.Label_PlaceHolder1.grid(row=1, column=0)
        self.root.Label_PlaceHolder2.grid(row=2, column=0)
        self.root.Label_PlaceHolder3.grid(row=3, column=0)
        self.root.Label_PlaceHolder4.grid(row=4, column=0)
        self.root.buttonAdd_Black.grid(row=5, column=0,)
        self.root.buttonDel_Black.grid(row=5, column=1,)
        self.root.buttonFin_Black.grid(row=5, column=2,)
class ErrorNoneFound():
    # Window for when no node was found
    def __init__(self) -> None:
        r =  ResolutionWindow()     
        r.root.Label_ErrorNoneFound.grid(row=0, column=0, columnspan=3)
        tk.mainloop()
class StudentAdded(ErrorNoneFound):
    # Window for successful addition data to database
    def __init__(self):
        r =  ResolutionWindow()   
        r.root.Label_StudentAdded.grid(row=0, column=0, columnspan=3)
        tk.mainloop()
class StudentDeleted(ErrorNoneFound):
    # Window for successful deletion data from database
    def __init__(self):
        r =  ResolutionWindow()      
        r.root.Label_StudentRemoved.grid(row=0, column=0, columnspan=3)
        tk.mainloop()
class ErrorEmptyEntry():
    # Window for when user did not fill all entries
    def __init__(self):
        r =  ResolutionWindow()      
        r.root.Label_ErrorEmptyEntry.grid(row=0, column=0, columnspan=3)
        tk.mainloop()

class Node:
    def __init__(self, index: int, data: list, parent: 'Node | None', left: 'Node | None' = None, right: 'Node | None' = None, color: False | True = False):
        self.index = index      # Index
        self.data = [data]      # Data
        self.parent = parent    # Parent
        self.left = left        # Left child
        self.right = right      # Right child
        self.color = color      # Color

class BST:
    def __init__(self) -> None:
        self.root = None
         
    def find_closest_succcessor(self, root: Node | None) -> Node | None:
        # Finding closest succesor to a node
        if root is not None:
            if root.right is not None:
                return self.__smallest_value_in_subtree(root.right)
            else: return root
        else: return root
        
    def __smallest_value_in_subtree(self, root: Node) -> Node:
        # Finding smallest value in a subtree
        if root.left is not None:
            return self.__smallest_value_in_subtree(root.left)
        else: return root
        
    def find_closest_predecessor(self, root: Node | None) -> Node | None:
        # Finding closest succesor to a node
        if root is not None:
            if root.left is not None:
                return self.__smallest_value_in_subtree(root.left)
            else: return root
        else: return root
        
    def __biggest_value_in_subtree(self, root: Node) -> Node:
        # Finding smallest value in a subtree
        if root.right is not None:
            return self.__biggest_value_in_subtree(root.right)
        else: return root

    def find(self, index: int) -> Node | None:
        # Help method to either return found Node or None value if the Node is not present
        return self.__find(self.root, index)
    
    def __find(self, root: Node, index: int) -> Node | None:
        # Recurrently returning the found Node or None value
        if root is None:
            return None
        if root.index == index:
            return root
        elif root.index > index:
            return self.__find(root.left, index)
        elif root.index < index:
            return self.__find(root.right, index)

    def add(self, index: int, data: list) -> None:
        # Adding new node to our BST
        self.root = self.__add(self.root, None, index, data)
        # Checking the colors in our BST
        node = self.find(index)
        self.check_color_add(node)
        # Making sure that root is black
        self.root.color = True

    def __add(self, root: Node, parent: Node | None, index: int, data: list) -> Node:
        # Recurrently modifying branch, till we find None child to replace it with a new node
        if root is None:
            root = Node(index, data, parent)
        elif root.index > index:
            root.left = self.__add(root.left, root, index, data)
        elif root.index < index:
            root.right = self.__add(root.right, root, index, data)
        elif root.index == index:
            root.data.append(data)
        return root
            
    def check_color_add(self, node: Node) -> None:
        # Red-Black BST logic
        if node.color == True:
            return
        if node.parent is None or node.parent.color == True:
            return
        else:
            # Initiating nodes that we will use                        
            parent = node.parent                  
            grandparent = parent.parent         
            root = grandparent.parent 
            # Choosing correct operations based on the 'structure' of sub-branch: Grandparent - Parent - Node
            if parent.index > grandparent.index:
                # If 'uncle' of our node is Black(True) or None, we need to do rotations and recolor
                if grandparent.left is None or grandparent.left.color == True:
                    # Right-Left Rotation and recoloring
                    if node.index < parent.index:
                        self.R_rotation(node, parent, grandparent)
                        self.L_rotation(node, grandparent, root)
                        node.color = True
                        grandparent.color = False
                    else:
                    # Left Rotation and recoloring
                        self.L_rotation(parent, grandparent, root)
                        parent.color = True
                        grandparent.color = False
                # If 'uncle' of our node is Red(False), we just need to recolor few Nodes
                elif grandparent.left.color == False:
                    grandparent.left.color = True 
                    grandparent.right.color = True
                    # After recoloring we need to recheck 'gradparent' for Red-Red conflict
                    grandparent.color = False
                    self.check_color_add(grandparent) 
            # Mirrored operations
            elif parent.index < grandparent.index:
                # If 'uncle' of our node is Black(True) or None, we need to do rotations and recolor
                if grandparent.right is None or grandparent.right.color == True:
                    # Right Rotation and recoloring
                    if node.index < parent.index:
                        self.R_rotation(parent, grandparent, root)
                        grandparent.color = False
                        parent.color = True
                    else: 
                    # Left-Right Rotation and recoloring
                        self.L_rotation(node, parent, grandparent)
                        self.R_rotation(node, grandparent, root)
                        grandparent.color = False
                        node.color = True
                # If 'uncle' of our node is Red(False), we just need to recolor few Nodes
                elif grandparent.right.color == False:  
                    grandparent.left.color = True 
                    grandparent.right.color = True
                    # After recoloring we need to recheck 'gradparent' for Red-Red conflict  
                    grandparent.color = False
                    self.check_color_add(grandparent) 
    
    def R_rotation(self, node: Node, parent: Node, root: Node | None) -> None:
        # Clockwise Rotation
        if root is not None:
            if root.right == parent:
                root.right = node
            else: root.left = node
        else: self.root = node
        
        node.parent = root
        parent.left = node.right
        if node.right is not None:
            node.right.parent = parent
        node.right = parent  
        parent.parent = node
        
    def L_rotation(self, node: Node, parent: Node, root: Node | None) -> None:
        # Counter-clockwise Rotation
        if root is not None:
            if root.right == parent:
                root.right = node
            else: root.left = node
        else: self.root = node
        
        node.parent = root
        parent.right = node.left
        if node.left is not None:
            node.left.parent = parent
        node.left = parent
        parent.parent = node
              
    def close_database_to_txt(self, file_name) -> None:
        # Help function for writing the entire tree into .txt file
        file = open(file_name, "w")
        self.write(self.root, file)
        file.close()

    def write(self, root: Node, file) -> None:
        # Recurrently writing the entire tree into .txt file       
        file.write(" ".join(root.data[0])+"\n")
        if root.left is not None:
            self.write(root.left, file)
        if root.right is not None:
            self.write(root.right, file)

    def open_database_from_txt(self, file_name) -> None:
        # Loading the data from .txt to our database
        file = open(file_name, "r")
        for data in file:
            if data != "\n":
                # Creating our indexing value from the name and surname
                data = data.split()
                name = data[:2]
                name = " ".join(name)
                index = encode(name)
                database.add(index, data)
        file.close()

    def delete(self, node: Node) -> None:
        if node.right is not None:       
            # We cannot delete internal nodes (It would destroy Red/Black properties)
            new_node = self.find_closest_succcessor(node)
            node.index = new_node.index
            node.data = new_node.data
            self.delete(new_node)
        elif node.left is not None and node.right is None:
            # We cannot delete internal nodes (It would destroy Red/Black properties)
            new_node = self.find_closest_predecessor(node)
            node.index = new_node.index
            node.data = new_node.data
            self.delete(new_node)
        elif node.left is None and node.right is None:
            parent = node.parent
            # Special case for when we are deleting last node in our tree
            if parent is None:
                self.root = None
                return
            # If the node is a leaf-node and Red(False), we can delete it otherwise we need to do rotations and recolor some nodes to maintain Red-Black BST properties
            if node.color == True:
                self.check_color_del(node)
            # Deleting the node
            if node.index >= parent.index and (parent.left is None or parent.left.index < node.index):
                parent.right = None
            else: parent.left = None
                
            
    def check_color_del(self, node: Node) -> None:
        # Red-Black BST logic
        parent = node.parent
        # If we reccurently got to root of our BST we can stop recurrsion
        if parent == None:
            return
        # Choosing correct operations based on the 'structure' of sub-branch: Parent - Node - Node's Sibling - It's Children
        elif node.index <= parent.index and parent.right.index > node.index:   
            if ((parent.right.left is None or parent.right.left.color == True) and (parent.right.right is None or parent.right.right.color == True) and parent.right.color == True):
                parent.right.color = False
                if parent.color == True:
                    self.check_color_del(parent)
                else:
                    parent.color = True
            elif parent.right.color == False:
                parent.right.color = parent.color
                parent.color = False
                self.L_rotation(parent.right, parent, parent.parent)
                self.check_color_del(node)
            elif (parent.right.right is None or parent.right.right.color == True) and (parent.right.left is not None and parent.right.left.color == False) and parent.right.color == True:
                parent.right.color = False
                parent.right.left.color = True
                self.R_rotation(parent.right.left, parent.right, parent)
                self.check_color_del(node)
            elif parent.right.right.color == False and parent.right.color == True:
                parent.right.color = parent.color
                parent.color = True
                parent.right.right.color = True
                self.L_rotation(parent.right, parent, parent.parent)
        # Mirrored operations
        elif node.index >= parent.index and parent.left.index<node.index:
            if ((parent.left.left is None or parent.left.left.color == True) and (parent.left.right is None or parent.left.right.color == True) and parent.left.color == True):
                parent.left.color = False
                if parent.color == True:
                    self.check_color_del(parent)
                else:
                    parent.color = True
            elif parent.left.color == False:
                parent.left.color = parent.color
                parent.color = False
                self.R_rotation(parent.left, parent, parent.parent)
                self.check_color_del(node)
            elif (parent.left.left is None or parent.left.left.color == True) and (parent.left.right is not None and parent.left.right.color == False) and parent.left.color == True:
                parent.left.color = False
                parent.left.right.color = True
                self.L_rotation(parent.left.right, parent.left, parent)
                self.check_color_del(node)
            elif parent.left.left.color == False and parent.left.color == True:
                parent.left.color = parent.color
                parent.color = True
                parent.left.left.color = True
                self.R_rotation(parent.left, parent, parent.parent)

def encode(name: str) -> int:
    #Turning name and surname into hash using MurMurHash
    name = name.replace(" ", "")
    name = name.lower()
    name = name.strip()
    index = mmh3.hash128(name)
    return index

# Creating Database
database = BST()

# Set the name of a .txt file you want to work with
file_name = "prototyp.txt"

# Starting database
print("Database loading .txt file")
database.open_database_from_txt(file_name)

# Initiating GUI
GUI = AddWindow()

# After finishing work rewriting the database into .txt file
database.close_database_to_txt(file_name)
print("Database saved back into .txt file")
