                    #CKC ACADEMY, JHANSI
                    #IP (046) AISSCE 2024 PROJECT

# ANALYSING LITERACY RATE OF INDIA 

#IMPORTING MODULES
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# READING CSV FILE
df = pd.read_csv("literacy_rate.csv")

#MAIN PROGRAM 
def main_menu():
  """Displays the main menu and handles user selection."""
  ans = 'y'
  while ans == 'y' or ans == 'Y':
    print("=" * 80)
    print("C.K.C ACADEMY JHANSI")
    print("=" * 80)
    print("SUBMITTED TO :: MR. ATUL KUMAR SAHU")
    print("AISSCE : 2023 - 2024")
    print("INFORMATICS PRACTICES (CODE NO: 046) PROJECT")
    print("=" * 80)
    print("Select any one options listed below:: ")
    print("1. Data Visualization")
    print("2. Data Analysis")
    print("3. Exit")
    print("=" * 80)

    opt = input("Enter your choice: ")
    
# FOR ENABING DATA VISUAL
    if opt == '1':
      visuals()

# FOR ENABING DATA ANALYSING
    elif opt == '2':
      analysis()

# FOR EXIT
    elif opt == '3':
      confirm_exit = input("Do you really want to exit? (y/n): ")
      if confirm_exit == 'y' or confirm_exit == 'Y':
        print("Thank you! Exiting...")
        sys.exit()
    else:
      print("\nInvalid choice. Try again.")
      continue

    ans = input("Do you want to continue (y/n)? ")

def visuals(): # USED FOR VISUALISING THE DATA USING GRAPHS
  """Provides options for data visualization."""
  
  while True:
    print("=" * 45)
    print("DATA VISUALISING MENU")
    print("-" * 38)
    print("Select any one options listed below:: ")
    print("1. Line Chart for a Year")
    print("2. Bar Chart / Histogram for a Years")
    print("3. Pie Chart for a Year")
    print("4. Back to Main Menu")
    print("=" * 45)  

    choice = int(input("Enter your choice: "))

# FOR LINE CHART
    if choice == 1:
      year = input("Enter year of Literacy ; "
                   "(Enter the any one year from the following :: '1951', '1961', '1971', '1981', '1991', '2001', '2011' ) :: ")
      df_year = df.sort_values(by=[year])
      n = int(input("Enter number of states (1 - 39): "))
      print(df_year.head(n))
      df_year.plot(x="State/Union Territory", y=year, kind="line", rot=75)
      plt.xlabel("State/UT Name", color="b", fontsize=12)
      plt.ylabel("Literacy Rate (%)", color="b", fontsize=12)
      plt.title(f"Top {n} Indian States' Literacy Analysis (Year: {year})", color="r", fontsize=16)
      plt.show()

# FOR HISTORGRAM OR BAR CHART      
    elif choice == 2:
      year = input("Enter year of Literacy ; "
                   "(Enter the any one year from the following :: '1951', '1961', '1971', '1981', '1991', '2001', '2011' ) :: ")
      df.hist(column=year, color="r", edgecolor="black")
      plt.xlabel("Literacy Rate (%)", color="r", fontsize=12)
      plt.ylabel("Number of States", color="r", fontsize=12)
      plt.title(f"All Indian States' Literacy Analysis (Year: {year})", color="g", fontsize=16)
      plt.show()

# FOR PIE CHART      
    elif choice == 3:
      year = input("Enter year of Literacy ; "
                   "(Enter the any one year from the following :: '1951', '1961', '1971', '1981', '1991', '2001', '2011' ) :: ")
      df_year = df.sort_values(by=[year])
      n = int(input("Enter number of states (1 - 39): "))
      print(df_year.head(n))
      df_year.plot(x="State/Union Territory", y=year, kind="pie", rot=75)
      plt.xlabel("State/UT Name", color="r", fontsize=12)
      plt.ylabel("Literacy Rate (%)", color="r", fontsize=12)
      plt.title(f"Top {n} Indian States' Literacy Analysis (Year: {year})", color="g", fontsize=16)
      plt.show()

    elif choice == 4:
      break
    else:
      print("\nInvalid choice. Try again.")

def analysis(): # USED FOR ANALYSING THE DATA USING GRAPHS
  """Provides options for data analysis."""
  while True:
    print("=" * 80)
    print("DATA ANALYSIS MENU")
    print("-" * 80)
    print("1. Top Records")
    print("2. Bottom Records")
    print("3. State with Maximum Literacy Rate")
    print("4. Display Complete DataFrame")
    print("5. Minimum, Maximum, and Average Literacy in a Year")
    print("6. Back to Main Menu")
    print("=" * 80)

    ch_an = int(input("Enter your choice: "))

# FOR TOP RECORDS
    if ch_an == 1:
      n = int(input("Enter the number of records to display"
                    "(SELECT ONLY UPTO 36 RECORDS)"))
      print(f"\nTop {n} records from the DataFrame:")
      print(df.head(n))

# FOR BOTTOM RECORDS   
    elif ch_an == 2:
      n = int(input("Enter the number of records to display"
                    "(SELECT ONLY UPTO 36 RECORDS)"))
      print(f"\nBottom {n} records from the DataFrame:")
      print(df.tail(n))

# FOR STATE WITH MAXIMUM LITERACY RATE  
    elif ch_an == 3:
      yr = (input("Enter the any one year from the following :: '1951', '1961', '1971', '1981', '1991', '2001', '2011' :: "))
      max_literacy = df[yr].max()
      df_max = df[df[yr] == max_literacy]
      print(f"\nState with Maximum Literacy Rate in the year {yr}:")
      print(df_max)

# FOR DISPLAY COMPLETE DATAFRAME      
    elif ch_an == 4:
      print("\nComplete DataFrame:")
      print(df)
      
# FOR MAX, MIN, AVG LITERACY RATE IN YEAR OF INDIA      
    elif ch_an == 5:
      yr = (input("Enter the any one year from the following :: '1951', '1961', '1971', '1981', '1991', '2001', '2011' :: "))
      print(f"\nMaximum Literacy Rate in {yr}:")
      max_literacy = df[yr].max()
      df_max = df[df[yr] == max_literacy]
      print(df_max)
      print(f"\nMinimum Literacy Rate in {yr}:")
      min_literacy = df[yr].min()
      df_min = df[df[yr] == min_literacy]
      print(df_min)
      avg_literacy = df[yr].mean()
      print(f"\nAverage Literacy Rate in the year {yr}: {avg_literacy}")

# FOR MAIN MENU      
    elif ch_an == 6:
      break
    else:
      print("\nInvalid choice. Try again.")

# Run the main program
main_menu()
