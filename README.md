
# Breast Cancer Detection using Machine Learning

Welcome to the Breast Cancer Detection project! This application leverages advanced machine learning techniques to accurately predict whether a tumor is **malignant** or **benign** based on **biopsy data**. By using this tool, you can assist in the **early detection** of breast cancer, enhancing patient care and outcomes.

---

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Model Overview](#model-overview)
- [Features](#features)
- [Contributing](#contributing)


---

## Installation

To get started with this project, you'll need Python and pip installed on your machine. Follow these steps to set up the environment:

1. **Clone the repository:**
   ```bash
   https://github.com/nilkanth02/Breast-cancer-detection-using-ML.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd Breast-cancer-detection-using-ML
   ```

3. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the Streamlit app locally with the following command:

```bash
streamlit run app.py
```

Open your browser and navigate to `http://localhost` to interact with the application. Input the tumor features in the provided fields and click on **"Predict "** to see the results.

---

## Model Overview

The core of this project is powered by **XGBoost**, a highly effective gradient boosting algorithm. The model was trained on a comprehensive breast cancer dataset, achieving an impressive accuracy of **98.24%** on the test set.


### Key Highlights:
- **Fast and Scalable**: XGBoost is optimized for speed and performance.
- **Robust**: Handles missing data well and incorporates regularization to prevent overfitting.

---

## Features

This application uses the following 30 features for accurate predictions:

- **Mean Features**:
  - Mean Radius
  - Mean Texture
  - Mean Perimeter
  - Mean Area
  - Mean Smoothness
  - Mean Compactness
  - Mean Concavity
  - Mean Concave Points
  - Mean Symmetry
  - Mean Fractal Dimension

- **Error Features**:
  - Radius Error
  - Texture Error
  - Perimeter Error
  - Area Error
  - Smoothness Error
  - Compactness Error
  - Concavity Error
  - Concave Points Error
  - Symmetry Error
  - Fractal Dimension Error

- **Worst Features**:
  - Worst Radius
  - Worst Texture
  - Worst Perimeter
  - Worst Area
  - Worst Smoothness
  - Worst Compactness
  - Worst Concavity
  - Worst Concave Points
  - Worst Symmetry
  - Worst Fractal Dimension

---

## Contributing

We welcome contributions! If you'd like to improve this project or have suggestions, please feel free to submit a pull request or open an issue. Let's make healthcare better together!


## Contact

For any questions or feedback, you can reach out to:

- **Nilkanth D. Ahire** - [nilkanth8747@gmail.com](mailto:nilkanth8747@gmail.com)
- **GitHub Profile** - [nilkanth02](https://github.com/nilkanth02)

Thank you for checking out this project! Together, we can contribute to better breast cancer detection and awareness.
