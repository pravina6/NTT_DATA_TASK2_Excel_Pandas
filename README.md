##### **PROJECT 2 : Excel Data Processing Using Pandas**



1. ###### **Objective**



The objective of this project is to create a Python script using the Pandas library to:



* Read data from two Excel files
* Combine the data using a common column (Employee\_ID)
* Handle duplicate and missing values
* Write the merged result into a new Excel file



###### **2. Project Structure**



NTT\_Data\_Task\_2\_Excel\_Pandas

│

├── employee\_basic.xlsx        (Input File 1)

├── employee\_salary.xlsx       (Input File 2)

├── main.py                    (Python Script)

├── combined\_employee.xlsx     (Output File)

└── README.md                  (Documentation)



###### **3. Libraries Used**



**1) Pandas**



Pandas is used for:

* Reading Excel files into Data Frames
* Cleaning data (removing duplicates and handling missing values)
* Merging two datasets based on a common column
* Writing the final output to an Excel file



**2) openpyxl**



openpyxl is required by Pandas to:

* Read .xlsx Excel files
* Write data into Excel format



###### **4. How to Install Required Libraries**



* Open Command Prompt and run the following command



               **pip install pandas openpyxl**



This installs the necessary libraries for the project.





###### **5. How to Run the Project**



**STEP 1:**

* Place all the project files inside the same folder:

 

           **NTT\_Data\_Task\_2\_Excel\_Pandas**



**STEP 2**:

Open Command Prompt inside this folder:



* Open the folder
* Click on the address bar
* Type cmd
* Press Enter



**STEP 3:**

* Run the Python script using:



          **python main.py**



**STEP 4:**

* After running, a new file named



         **combined\_employee.xlsx**



   will be created automatically in the same folder.





###### **6. Explanation of main.py Script**



* The script reads both Excel files using **pd.read\_excel()**
* Duplicate rows are removed using **drop\_duplicates()**
* The two files are merged using **pd.merge()** on the column Emp\_ID
* Missing values are handled using **fillna()**
* The final merged data is written into a new Excel file using **to\_excel()**



###### **7. Input Files**



**employee\_basic.xlsx**





| **Emp\_ID**| **Name**   | **Department** |

|-------|--------|------------|

| 101   | Maya R | IT         |

| 102   | Arjun  | HR         |

| 103   | Meena  | Finance    |



**employee\_salary.xlsx**



|**Emp\_ID** | **Salary** | **Location**  |

|-------|--------|-----------|

| 101   | 60000  | Chennai   |

| 102   | 55000  | Bangalore |

| 103   | 65000  | Hyderabad |





###### **8. Output File** 



**combined\_employee.xlsx**



|**Emp\_ID** | **Name**   | **Department** | **Salary** | **Location**  |

|-------|--------|------------|--------|-----------|

| 101   | Maya R | IT         | 60000  | Chennai   |

| 102   | Arjun  | HR         | 55000  | Bangalore |

| 103   | Meena  | Finance    | 65000  | Hyderabad |



###### **9. Conclusion**



This project demonstrates how Python Pandas can be effectively used for Excel data processing, data cleaning, and merging datasets based on a common key.

