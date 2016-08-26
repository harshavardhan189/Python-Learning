# -*- coding: utf-8 -*-
"""
Created on Wed Aug 24 23:42:59 2016

Deque with Two Way Linked Dictionaries
@author: harsha
"""
    
class Node():
    
    def __init__(self):
        self.data = {}
    
    def setData(self,data,nodenum):
        self.data["data"] = data
        self.data["nodenum"] = nodenum
        
    def getData(self):
        return self.data["data"]

    def setNext(self,nextNode):
        self.data["next"] = nextNode

    def getNext(self):
        return self.data["next"]
     
    def getPrevious(self):
        return self.data["prev"]
        
    def setPrevious(self,prevNode):
        self.data["prev"] = prevNode        


class LinkedDeque():
    
    def __init__(self):
        self.tail = None
        self.head = None
        
    def isEmpty(self):
        return self.head == None
        
    def getLen(self):
        current_node = self.head
        current_length = 0

        while current_node != None:
            current_length = current_length + 1
            current_node = current_node.getNext()       
        return current_length
    
    def fdqueue(self):
        if self.head != None:
            popped_node = self.head
            self.head = self.head.getNext()

            try:
                self.head.setPrevious(None)
            except:
                self.tail = None
            
            popped_node.setNext(None)
            return popped_node.getData()
        else:
            return None

    def rdqueue(self):
        if self.tail != None:
            popped_node = self.tail
            self.tail = self.tail.getPrevious()
            try:
                self.tail.setNext(None)
            except:
                self.head = None
            popped_node.setPrevious(None)
            return popped_node.getData()
        else:
            return None
        
    def fenqueue(self,data):
        nodeNum = self.getLen()
        tempNode = Node()
        tempNode.setData(data,nodeNum)
        
        if self.head is None:
            tempNode.setPrevious(self.head)
            tempNode.setNext(self.tail)
            self.tail = tempNode
        else:
            tempNode.setNext(self.head)
            self.head.setPrevious(tempNode)
            tempNode.setPrevious(None)
        self.head = tempNode

    def renqueue(self,data):
        nodeNum = self.getLen()
        tempNode = Node()
        tempNode.setData(data,nodeNum)
        
        if self.tail is None:
            tempNode.setNext(self.tail)
            tempNode.setPrevious(self.head)
            self.head = tempNode
        else:
            tempNode.setPrevious(self.tail)
            self.tail.setNext(tempNode)
            tempNode.setNext(None)
        self.tail = tempNode
