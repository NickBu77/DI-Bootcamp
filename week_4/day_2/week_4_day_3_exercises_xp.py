{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "1c8d52bd",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "import seaborn as sns\n",
    "from IPython.display import Image\n",
    "\n",
    "\n",
    "# Setting up max columns & rows displayed to 100\n",
    "pd.options.display.max_columns = 100\n",
    "pd.options.display.max_rows = 250"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "efb8172a",
   "metadata": {},
   "source": [
    "🌟 Exercise 1 : Import A File From Kaggle\n",
    "Instructions\n",
    "Import the titanic dataset that you can find on Kaggle.\n",
    "Print the first few rows of the DataFrame."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "4890ccc5",
   "metadata": {},
   "outputs": [],
   "source": [
    "Titanic_db = pd.read_csv('Titanic-Dataset.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "334d8eb1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>PassengerId</th>\n",
       "      <th>Survived</th>\n",
       "      <th>Pclass</th>\n",
       "      <th>Name</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Age</th>\n",
       "      <th>SibSp</th>\n",
       "      <th>Parch</th>\n",
       "      <th>Ticket</th>\n",
       "      <th>Fare</th>\n",
       "      <th>Cabin</th>\n",
       "      <th>Embarked</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Braund, Mr. Owen Harris</td>\n",
       "      <td>male</td>\n",
       "      <td>22.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>A/5 21171</td>\n",
       "      <td>7.2500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Cumings, Mrs. John Bradley (Florence Briggs Th...</td>\n",
       "      <td>female</td>\n",
       "      <td>38.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>PC 17599</td>\n",
       "      <td>71.2833</td>\n",
       "      <td>C85</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>Heikkinen, Miss. Laina</td>\n",
       "      <td>female</td>\n",
       "      <td>26.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>STON/O2. 3101282</td>\n",
       "      <td>7.9250</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Futrelle, Mrs. Jacques Heath (Lily May Peel)</td>\n",
       "      <td>female</td>\n",
       "      <td>35.0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>113803</td>\n",
       "      <td>53.1000</td>\n",
       "      <td>C123</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>0</td>\n",
       "      <td>3</td>\n",
       "      <td>Allen, Mr. William Henry</td>\n",
       "      <td>male</td>\n",
       "      <td>35.0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>373450</td>\n",
       "      <td>8.0500</td>\n",
       "      <td>NaN</td>\n",
       "      <td>S</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   PassengerId  Survived  Pclass  \\\n",
       "0            1         0       3   \n",
       "1            2         1       1   \n",
       "2            3         1       3   \n",
       "3            4         1       1   \n",
       "4            5         0       3   \n",
       "\n",
       "                                                Name     Sex   Age  SibSp  \\\n",
       "0                            Braund, Mr. Owen Harris    male  22.0      1   \n",
       "1  Cumings, Mrs. John Bradley (Florence Briggs Th...  female  38.0      1   \n",
       "2                             Heikkinen, Miss. Laina  female  26.0      0   \n",
       "3       Futrelle, Mrs. Jacques Heath (Lily May Peel)  female  35.0      1   \n",
       "4                           Allen, Mr. William Henry    male  35.0      0   \n",
       "\n",
       "   Parch            Ticket     Fare Cabin Embarked  \n",
       "0      0         A/5 21171   7.2500   NaN        S  \n",
       "1      0          PC 17599  71.2833   C85        C  \n",
       "2      0  STON/O2. 3101282   7.9250   NaN        S  \n",
       "3      0            113803  53.1000  C123        S  \n",
       "4      0            373450   8.0500   NaN        S  "
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Titanic_db.head(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d4c7f065",
   "metadata": {},
   "source": [
    "🌟 Exercise 2: Importing A CSV File\n",
    "Instructions\n",
    "Use the Iris Dataset CSV.\n",
    "- Download the Iris dataset CSV file and place it in the same directory as your Jupyter Notebook.\n",
    "- Import the CSV file using Pandas.\n",
    "- Display the first five rows of the dataset."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "fd9ff472",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>5.1</th>\n",
       "      <th>3.5</th>\n",
       "      <th>1.4</th>\n",
       "      <th>0.2</th>\n",
       "      <th>Iris-setosa</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>4.9</td>\n",
       "      <td>3.0</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>4.7</td>\n",
       "      <td>3.2</td>\n",
       "      <td>1.3</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>4.6</td>\n",
       "      <td>3.1</td>\n",
       "      <td>1.5</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>5.0</td>\n",
       "      <td>3.6</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5.4</td>\n",
       "      <td>3.9</td>\n",
       "      <td>1.7</td>\n",
       "      <td>0.4</td>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   5.1  3.5  1.4  0.2  Iris-setosa\n",
       "0  4.9  3.0  1.4  0.2  Iris-setosa\n",
       "1  4.7  3.2  1.3  0.2  Iris-setosa\n",
       "2  4.6  3.1  1.5  0.2  Iris-setosa\n",
       "3  5.0  3.6  1.4  0.2  Iris-setosa\n",
       "4  5.4  3.9  1.7  0.4  Iris-setosa"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'\n",
    "\n",
    "iris_db = pd.read_csv(url)\n",
    "\n",
    "iris_db.head(5)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c433abaa",
   "metadata": {},
   "source": [
    "🌟 Exercise 3: Reading JSON Data\n",
    "Instructions\n",
    "Use a sample JSON dataset\n",
    "\n",
    "Import the JSON data from the provided URL.\n",
    "Use Pandas to read the JSON data.\n",
    "Display the first five entries of the data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "f8b892ee",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>userId</th>\n",
       "      <th>id</th>\n",
       "      <th>title</th>\n",
       "      <th>body</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>sunt aut facere repellat provident occaecati e...</td>\n",
       "      <td>quia et suscipit\\nsuscipit recusandae consequu...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>2</td>\n",
       "      <td>qui est esse</td>\n",
       "      <td>est rerum tempore vitae\\nsequi sint nihil repr...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>ea molestias quasi exercitationem repellat qui...</td>\n",
       "      <td>et iusto sed quo iure\\nvoluptatem occaecati om...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>4</td>\n",
       "      <td>eum et est occaecati</td>\n",
       "      <td>ullam et saepe reiciendis voluptatem adipisci\\...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>5</td>\n",
       "      <td>nesciunt quas odio</td>\n",
       "      <td>repudiandae veniam quaerat sunt sed\\nalias aut...</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   userId  id                                              title  \\\n",
       "0       1   1  sunt aut facere repellat provident occaecati e...   \n",
       "1       1   2                                       qui est esse   \n",
       "2       1   3  ea molestias quasi exercitationem repellat qui...   \n",
       "3       1   4                               eum et est occaecati   \n",
       "4       1   5                                 nesciunt quas odio   \n",
       "\n",
       "                                                body  \n",
       "0  quia et suscipit\\nsuscipit recusandae consequu...  \n",
       "1  est rerum tempore vitae\\nsequi sint nihil repr...  \n",
       "2  et iusto sed quo iure\\nvoluptatem occaecati om...  \n",
       "3  ullam et saepe reiciendis voluptatem adipisci\\...  \n",
       "4  repudiandae veniam quaerat sunt sed\\nalias aut...  "
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "url = 'https://jsonplaceholder.typicode.com/posts'\n",
    "\n",
    "json_data = pd.read_json(url)\n",
    "json_data[0:5]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8aa66000",
   "metadata": {},
   "source": [
    "🌟 Exercise 4: Loading Data From An Excel File\n",
    "Instructions\n",
    "Take this excel file for practice.\n",
    "- Download the sample Excel file and place it in your working directory.\n",
    "- Use Pandas to read the Excel file.\n",
    "- Display the first few rows of the data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "ea2a8624",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>0</th>\n",
       "      <th>First Name</th>\n",
       "      <th>Last Name</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Country</th>\n",
       "      <th>Age</th>\n",
       "      <th>Date</th>\n",
       "      <th>Id</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Dulce</td>\n",
       "      <td>Abril</td>\n",
       "      <td>Female</td>\n",
       "      <td>United States</td>\n",
       "      <td>32</td>\n",
       "      <td>15/10/2017</td>\n",
       "      <td>1562</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Mara</td>\n",
       "      <td>Hashimoto</td>\n",
       "      <td>Female</td>\n",
       "      <td>Great Britain</td>\n",
       "      <td>25</td>\n",
       "      <td>16/08/2016</td>\n",
       "      <td>1582</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Philip</td>\n",
       "      <td>Gent</td>\n",
       "      <td>Male</td>\n",
       "      <td>France</td>\n",
       "      <td>36</td>\n",
       "      <td>21/05/2015</td>\n",
       "      <td>2587</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Kathleen</td>\n",
       "      <td>Hanner</td>\n",
       "      <td>Female</td>\n",
       "      <td>United States</td>\n",
       "      <td>25</td>\n",
       "      <td>15/10/2017</td>\n",
       "      <td>3549</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   0 First Name  Last Name  Gender        Country  Age        Date    Id\n",
       "0  1      Dulce      Abril  Female  United States   32  15/10/2017  1562\n",
       "1  2       Mara  Hashimoto  Female  Great Britain   25  16/08/2016  1582\n",
       "2  3     Philip       Gent    Male         France   36  21/05/2015  2587\n",
       "3  4   Kathleen     Hanner  Female  United States   25  15/10/2017  3549"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "url = 'file_example_XLS_10.xls'\n",
    "\n",
    "exceldata = pd.read_excel(url)\n",
    "exceldata[0:4]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a9c41776",
   "metadata": {},
   "source": [
    "🌟 Exercise 5 : Export A Dataframe To Excel Format And JSON Format.\n",
    "Instructions\n",
    "Create a simple dataframe.\n",
    "Export the dataframe to an excel file.\n",
    "Export the dataframe to a JSON file."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "c0a282ba",
   "metadata": {},
   "outputs": [],
   "source": [
    "sample_data = {'animals' : ['cat','dog','leopard','rhyno'],\n",
    "               'currencies' : ['dollar','shekels','pounds','yen'],\n",
    "               'names' : ['ryan','bob','crow','lev'] }"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "33b4cf70",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>animals</th>\n",
       "      <th>currencies</th>\n",
       "      <th>names</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>cat</td>\n",
       "      <td>dollar</td>\n",
       "      <td>ryan</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>dog</td>\n",
       "      <td>shekels</td>\n",
       "      <td>bob</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>leopard</td>\n",
       "      <td>pounds</td>\n",
       "      <td>crow</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>rhyno</td>\n",
       "      <td>yen</td>\n",
       "      <td>lev</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   animals currencies names\n",
       "0      cat     dollar  ryan\n",
       "1      dog    shekels   bob\n",
       "2  leopard     pounds  crow\n",
       "3    rhyno        yen   lev"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sample_df = pd.DataFrame(sample_data)\n",
    "sample_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "2075f1e8",
   "metadata": {},
   "outputs": [],
   "source": [
    "sample_df.to_csv('sample_df.csv',index=False)\n",
    "sample_df.to_json('sample_df.json',orient='records')"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
