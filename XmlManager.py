'''
====================================================================
Library for XML structure
(C) Copyright 2019
====================================================================
'''
__author__  = 'ELAIRAJ Mohamed'
__version__ = '1.0.0'
__email__   = 'med.elairaj@gmail.com'

'''
CHANGE LOG
==========
1.0.0 First Draft  XmlManager Structure class
1.0.1 Add function to handle the feature
==========
'''

import xml.etree.cElementTree as ET
from xml.dom import minidom
import datetime
import shutil
import os
import sys



# Version of the  XML structure. Increase it if modified.
XML_VERSION = '1.0.1'




class XmlManager():
    '''
    This class is the base class for the Xml Structure classe.
    '''

    #def __init__(self,user,Tbudget,Sbudget,Category,Date,Comment):
    def __init__(self,user,Tbudget,DataUserInformation=[]):
        '''
        Description: Constructor.
        '''
        self.user = user                #User
        self.Tbudget = Tbudget          #Target
        self.DataUserInformation = DataUserInformation      #DataUserInformation 
        self.ActualBudget = 0
                              
        # self.Sbudget = Sbudget                            #Spent
        # self.Category = Category                          #Category
        # self.Date = Date                                  #Date
        # self.Comment = Comment                            #Comment

    def CreateStructure(self):
        '''
        Description: Create an XML file
        '''
        # Generate the XML structure
        Owner = ET.Element(self.user)
        Owner_TB = ET.SubElement(Owner, "TargetBudget", TargetBudget = self.Tbudget)
        for Sbudget,Ctgy,Date_Time,Comments in self.DataUserInformation:
            Owner_Data = ET.SubElement(Owner, "MoneySpentInformations", SpentMoney = Sbudget, Category = Ctgy, Date = Date_Time,Comment = Comments)
        Owner_AB = ET.SubElement(Owner, "Budget", ActualBudget = self.TotalSpentMoney())     
        tree = ET.ElementTree(Owner)
        tree.write(self.user+"File.xml")
        print("Done !!")
        

    def UpdateStructure(self):
        '''
        Description : Update structure
        '''
        print("Update function")

    def TotalSpentMoney(self):
        '''
        Description : Calculate Total Spent Money
        '''
        TotalSM = 0
        for Sbudget in self.DataUserInformation:
            TotalSM = TotalSM + int(Sbudget[0])
        
        _ActualBudget = int(self.Tbudget) - TotalSM
        
        return str(_ActualBudget)

    def AddDataInformationElement(self,AddDataInformationElement=[]):
        '''
        Description : Delete a customised category
        '''
        # tree = ET.ElementTree(file =self.user+'File.xml')
        # root = tree.getroot()
        # print(root.tag)

        # if root.tag == self.user:
        #     print("AddDataInformationElement : ",AddDataInformationElement)
        #     for Sbudget,Ctgy,Date_Time,Comments in AddDataInformationElement:
        #         Owner_Data = ET.SubElement(root, "MoneySpentInformations", SpentMoney = Sbudget, Category = Ctgy, Date = Date_Time,Comment = Comments)
        #     Owner_AB = ET.SubElement(root, "ActualBudget", ActualBudget = self.TotalSpentMoney())
        #     tree.write(self.user+"File.xml")

    def __GetValue__(self):
        '''
        Description : Get a Current Solde
        '''
        print("Current Solde")
    
    def __SetValue__(self):
        '''
        Description : Set a Spent money
        '''
        print("Spent money")

class XmlBalise():
    '''
    This class is the base class for the Xml Structure classe.
    '''

    def __init__(self):
        '''
        Description: Constructor. Creates several common tags.
        '''
        print ("init")