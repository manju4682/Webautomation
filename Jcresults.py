from selenium import webdriver
import csv

def get_results(driver,details):
    
    #Accessing the site
    driver.get('http://results.jssstuniv.in/')

    #opening the write file
    with open('results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USN", "Name", "CS510","CS520","CS530","CS540","CS57L","CS58L","Elective1","Elective2"])

        #opening
        with open(details, 'r') as details_file:
            reader = csv.reader(details_file , delimiter = ',')
            next(reader) #Skipping the header

            #Retrieving the results for each USN in the details file
            for row in reader:
                li = []
                sendusn = driver.find_element_by_xpath('//*[@id="USN"]')

                #This might change. Depends on the structure of the file.
                sendusn.send_keys(row[1])
                button =  driver.find_element_by_xpath('/html/body/div/form/button')
                button.click()

                #This try block prevents from break in execution if results for a particular usn is not found
                try:
                    name = driver.find_element_by_xpath('//*[@id="HTMLtoPDF"]/center/h1')
                    usn = driver.find_element_by_xpath('//*[@id="HTMLtoPDF"]/center/h2')
                    li.append(usn.text)
                    li.append(name.text)
                    results = driver.find_elements_by_xpath('//*[@id="HTMLtoPDF"]/table/tbody/tr')
                    if(results[0].text.split()[0]!="CS510"):
                        backbutton = driver.find_element_by_xpath('/html/body/center/div/form[2]/button')   
                        backbutton.click() 
                        continue
                    else:
                        for i in results:
                            res = i.text.split()
                            li.append(res[-1])

                        #Writing the results to CSV file    
                        writer.writerow(li)  

                    #going back to search for new result    
                    backbutton = driver.find_element_by_xpath('/html/body/center/div/form[2]/button')   
                    backbutton.click() 
                except:
                    driver.close()
                    driver  = webdriver.Chrome()
                    driver.get('http://results.jssstuniv.in/')

if __name__ == '__main__':    

    driver  = webdriver.Chrome()

    #The details file should be sent.
    get_results(driver,"details.csv")
    driver.quit()
