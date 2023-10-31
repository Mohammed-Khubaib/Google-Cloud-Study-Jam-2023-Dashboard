import pandas as pd

# Load the CSV data into a DataFrame


def Sort_List(Ndf) :
    # List of names to sort by
    names_to_sort_by = [
        "Vasampally Sagar",
        "Bandra Anusha",
        "Kaparthi Shreya",
        "Abrar Sharif",
        "Mohammed Khubaib",
        "Kakarlapudi Madhuri",
        "K Sai Priya",
        "Chaitra Dayyala",
        "G.Surya Poojavi",
        "Sneha Chowdary",
        "D Shivakumar",
        "H Pooja",
        "Sanjana Appam",
        "G.Chandrika",
        "K.Vaishnavi",
        "Garrepalli Shivani",
        "Mohammed Adnan Yunus",
        "Kasoji Tulasi Bhavani",
        "A.pavan kalyan goud",
        "Izma Fatima",
        "Ankur Badhwar",
        "Nuthulakanti.Nithish Reddy",
        "P . Harshini Naidu",
        "Vontari sathwika",
        "zain hassan",
        "Aditya Dass",
        "Vinay Dayama",
        "Mohammed Uzair",
        "Mohammed Ilyaan",
        "Zahra Hussaini Syeda",
        "Sripriya Jaju",
        "Mohammed Waseem Khan",
        "Marpu Sandeep",
        "C pruthvinath reddy",
        "Adithya Chilupuri",
        "Madeeha Majid",
        "Syed Saarib Rasheed",
        "Mitta Gowri Sri Vani",
        "Yahya Mohammed",
        "Rayyan Ahmed",
        "FAYAZ FAZAL KHAN",
        "Abdur Rahman Qasim",
        "Peddinenikaluva kundana",
        "KISHORE KUMAR REDDY PEBBETI",
        "Motassim Mohammed Meraj Khan",
        "Abdullah Mohammed Khan",
        "S Mihir mudiraj",
        "M.Sathwika",
        "Mohammed Abrar Ali",
        "Kandi Chandana",
        "Pachipala Sai Divyansi",
        "Fareed Ahmed Owais",
        "Umair Ahmed",
        "Fatima Mohammed Khan",
        "Omair Mohiuddin",
        "Hasita Kasturi",
        "Abhishek gupta",
        "Saniya Afreen",
        "Qudsia Naaz",
        "Soha Ali Khan",
        "Vyshnavi krishna dasari",
        "Syed Abdullah Ayeman",
        "Mohammed Abdul Hannan Muntasir",
        "Abhinav Kalyan",
        "Hana Yadullah",
        "Rohit Sai Sharan B",
        "Rangari Aravind",
        "Majeti Sadhana",
        "Salvaji bhuvan",
        "vijnendra kopuri",
        "Tauqeer ali",
        "Bhavya Rambappagari",
        "Mohammed Yahya Ahmed",
        "Pantangi Maruthi",
        "Asfia fathima",
        "NALLA SHRIYA REDDY",
        "Puram Vamshi",
        "Syed Asfaan Hussain",
        "Gulam Mahmood Qureshi",
        "Dhanush",
        "Thakur Aryan Singh",
        "Saketh",
        "P.R Rhishabh"
        "Imran Peddinti",
    ]

    # Create a custom sorting key using the index of names in the list
    Ndf['Sort Key'] = Ndf['Student Name'].apply(lambda x: names_to_sort_by.index(x) if x in names_to_sort_by else len(names_to_sort_by))

    # Sort the DataFrame by the custom sorting key
    Ndf = Ndf.sort_values(by=['Sort Key'])

    # Drop the 'Sort Key' column if you don't need it in the final output
    Ndf = Ndf.drop(columns=['Sort Key'])

    # return the sorted data to a new CSV file
    return Ndf