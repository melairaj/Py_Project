# Test Code

from XmlManager import XmlManager

# Input Informations
Info =[('5','Loisirs','01-01-2020','Escalade'),('10','Shopping','02-01-2020','Sanintaire'),('20','Etudes','03-01-2020','Cahiers'),('500','Immobilier','05-01-2020','Logement')]
InfoElement =[('20','Loisirs','10-01-2020','Randonné')]
InfoElement1 =[('0','0','0','0')]

#APIs
FrstStructure = XmlManager('MElairaj','1000',Info)
FrstStructure.CreateStructure()