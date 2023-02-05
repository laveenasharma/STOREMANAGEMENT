def readInvoice():
    invoiceObject = open("customerInvoice.csv", "r")
    for customer in invoiceObject:
        customerInvoiceArray = customer.split(",")
    newInvoiceId = int(customerInvoiceArray[0]) + 1 
    invoiceObject.close()   
    return newInvoiceId

def writeInvoice(name,phnNo):
    newID = readInvoice()
    invoiceObject = open("customerInvoice.csv", "a")    
    invoiceObject.write("\n" + str(newID) + "," + name + "," + phnNo)    
    invoiceObject.close()
    return newID, phnNo

def productLists ():
# Reading proObject
    proObject = open("product.csv", 'r')
    for proIndex in proObject:
        print(proIndex)
    proObject.close()
    # taking input from the customer
    productId =input("Enter the Product ID:")
    productQuantity = int(input("Enter the Quantity for the Product"))
    proObject = open("product.csv", 'r')
    for proIndex in proObject:
        proArray = proIndex.split(",")
        #print(proArray[0])
        productIdArray = proArray[0]
        if proArray[0]== productId:
            price=int(proArray[2])
            # print(proArray[2])
            total= productQuantity * price
            return productIdArray, productQuantity, total
            #break
    proObject.close()

def writeTransaction(customer, product):
    fileObject=open("Transaction.csv", "a")
    newLine=("\n"+str(customer[0])+","+str(customer[1])+","+str(product[0])+","+str(product[1])+","+str(product[2]))
    fileObject.write(newLine)
    fileObject.close()
    return customer[0]

def printInvoice(newInvoiceId):
    #global totalPayments 
    totalPayments = 0
    fileOpen = open("Transaction.csv", "r")
    for invoiceIndex in fileOpen:
        invoiceArray = invoiceIndex.split(",")
        
        if (invoiceArray[0] == str(newInvoiceId)):
            totalPayments += int(invoiceArray[4])
        
    print("Final Invoice Details for the Customer is: ", totalPayments)
           

def readTransaction():
    fileObj=open("Transaction.csv","r")
    invoiceTotal=0
    for fileIndex in fileObj:
        fileArray = fileIndex.split(",")
    
        print(fileArray)
    
    fileObj.close()


for storeManagement in range (100):    
    inputData=input("Is it a new invoice? (Y/N): ")
    if inputData=="Y" or inputData=="y":
        productFlag="Y"
        customerName = input("Enter the Name of the Customer:")
        customerContactNumber = input("Enter the Mobile No.: ")
        customer=writeInvoice(customerName,customerContactNumber)
        #totalPayments = 0
        InvoiceId = readInvoice() - 1
        while productFlag=="Y":
            product=productLists ()
            writeTransaction(customer, product)
            productFlag=input("Do you need more products? (Y/N): ")
        printInvoice(InvoiceId)
    else:
        readTransaction()

