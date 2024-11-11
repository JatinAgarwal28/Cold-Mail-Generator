Sure! Below is a professional README template for your Cold Mail Generator project. This README includes sections typically found in a professional README file, such as project description, features, installation instructions, usage, and technologies used.

---

# 📧 Cold Mail Generator

A Streamlit-based web application designed to help users generate personalized cold emails for job applications. By uploading a CV and providing a job listing URL, the application extracts relevant job details, queries the user's portfolio for relevant links, and generates a tailored email using a language model.

## Features

- **File Upload**: Upload your CV in PDF format.
- **URL Input**: Provide a URL to a job listing.
- **Job Extraction**: Extracts job roles, experience, skills, and descriptions from the provided URL.
- **Portfolio Querying**: Uses ChromaDB to find relevant portfolio links based on job requirements.
- **Email Generation**: Generates a cold email using the extracted job details, portfolio links, and CV content.

## Technologies Used

- **Streamlit**: For the web interface.
- **Langchain**: For processing text and interacting with the language model.
- **ChromaDB**: For storing and querying portfolio data.
- **ChatGroq**: The language model used for job extraction and email generation.
- **Pandas**: For handling CSV files containing portfolio data.
- **PyPDFLoader**: For reading and processing PDF CVs.
- **WebBaseLoader**: For scraping job listing data from the provided URL.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/cold-mail-generator.git
    cd cold-mail-generator
    ```

2. **Create a virtual environment and activate it**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    - Create a `.env` file in the project root directory and add your API key:
        ```
        GROQ_API_KEY=your_groq_api_key
        ```

5. **Run the application**:
    ```sh
    streamlit run app.py
    ```

## Usage

1. **Upload Your CV**: Use the file uploader to upload your CV in PDF format.
2. **Enter Job Listing URL**: Input the URL of the job listing you are interested in.
3. **Submit**: Click the submit button to generate a personalized cold email based on the job details and your CV.
4. **Review Generated Email**: The generated email will be displayed on the screen. You can copy it and use it to apply for the job.

## Project Structure

```
cold-mail-generator/
│
├── chains.py             # Chain class for job extraction and email generation
├── portfolio.py          # Portfolio class for loading and querying portfolio data
├── utils.py              # Utility functions, including clean_text
├── app.py                # Main Streamlit application
├── requirements.txt      # List of required Python packages
└── README.md             # Project README file
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Replace `yourusername`, `your_groq_api_key`, and `your-email@example.com` with your actual GitHub username, API key, and email address. This README provides a comprehensive overview of the project, installation steps, usage instructions, and contact information.
