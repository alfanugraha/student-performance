# Student Performance Project

## Project Overview

This repository contains the code and documentation for the student performance analysis project, which is part of the MLZoomcamp Capstone Project 1. The project utilizes the "Student Performance" dataset from the UCI Machine Learning Repository to analyze and predict student grades based on various features.

Cortez, P. (2008). Student Performance [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5TG7T.

## Dataset

The dataset used in this project can be found at the UCI Machine Learning Repository: [Student Performance Data Set](https://archive.ics.uci.edu/dataset/320/student+performance). It contains various attributes related to student demographics, social and school-related features, and their grades.

## Project Structure

```
└── 📁student-performance
    └── 📁data
        ├── student-mat.csv
        ├── student-merge.R
        ├── student-por.csv
        ├── student.txt
    └── 📁images
        ├── app.png
    └── 📁notebook
        ├── best_model.pkl
        ├── student_performance.ipynb
    └── 📁scripts
        ├── dtree_model.pkl
        ├── predict-test.py
        ├── predict.py
        ├── train.py
    ├── app.py
    ├── Dockerfile
    ├── LICENSE
    ├── Pipfile
    ├── Pipfile.lock
    ├── README.md
    └── requirements.txt
```

## Reproducibility 

### System Requirements

- Python 3.12 or higher
- Docker (optional, for containerized setup)
- Streamlit (for web app deployment)

### Local Setup

To get started with the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/alfanugraha/student-performance.git
   ```
2. Navigate to the project directory:
   ```bash
    cd student-performance
    ```

3. Install the required dependencies:
   ```bash
   pipenv install
   ```

4. Run the model
   ```bash
   pipenv run python scripts/predict.py
   ```

5. Test the model with test data
   ```bash
   pipenv run python scripts/predict-test.py
   ```

### Streamlit App Preview

Run streamlit webapps (optional) with the following command:

```bash
pipenv run streamlit run app.py --server.port 8501
```

![Streamlit App Preview](./images/app.png)

To access the app, open your web browser and navigate to `http://localhost:8501`

### Docker Container

1. Build the Docker image:
   ```bash
   docker build -t student-performance .
   ```

2. Run the Docker container:
   ```bash
   docker run -p 9696:9696 student-performance
   ```
   Flask API will be accessible at `http://localhost:9696/predict`

3. Test the model
   ```bash
   python scripts/predict-test.py
   ```

### Cloud Deployment



## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- The dataset is provided by the UCI Machine Learning Repository.
- Kaggle by Nezahat Korkmaz: [https://www.kaggle.com/code/nezahatkk/uci-gradient-boosting-student-performance-dataset](https://www.kaggle.com/code/nezahatkk/uci-gradient-boosting-student-performance-dataset)
- This project is part of the MLZoomcamp Capstone Project 1.
- Special thanks to the MLZoomcamp community for their support and resources.
