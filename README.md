# Blog-Generator-Using-Langchain-Streamlit-and-llama2 Model

## Overview

This Streamlit application utilizes the LLama 2 model to generate blog content based on user inputs. Users can specify the blog topic, word limit, and target job profile to tailor the content accordingly. The application provides a simple and interactive interface for quickly generating blogs with AI assistance.

## Features

- **Blog Topic Input**: Users can enter the desired topic for the blog.
- **Word Limit**: Users can specify the maximum word count for the blog.
- **Target Audience Selector**: Users can choose the intended audience or job profile for which the blog is being written, such as Data Scientist, AI Researcher, or Common People.
- **Responsive UI**: The application is designed to be user-friendly and responsive, making it easy to use on various devices.

## Requirements

To run this application, you will need the following Python libraries:

- `streamlit`
- `langchain`
- `langchain-community`

Install these dependencies using the following command:

```sh
pip install streamlit langchain langchain-community
```

## Usage

To start the application:

1. Clone this repository to your local machine.
2. Navigate to the directory containing the application files.
3. Run the Streamlit application with the command:

```sh
streamlit run app.py
```

4. The application will open in your default web browser.

## How It Works

The application uses a simple Streamlit interface to collect user inputs for the blog topic, word limit, and job profile. Upon clicking the "Generate" button, the LLama 2 model is invoked with a customized prompt that includes the provided details. The model then generates a blog post that fits within the specified parameters.

## Example

Here's an example of how to use the application:

1. Enter the blog topic in the text input field.
2. Specify the word limit for the blog.
3. Select the job profile for which the blog is intended from the dropdown menu.
4. Click the "Generate" button to produce the blog content.

The generated blog will be displayed below the button.

## License

Please ensure to review the license agreement and usage policy of the LLama 2 model before using this application.

## Contributing

Contributions to this project are welcome. Please submit a pull request or open an issue if you have suggestions for improvements or have encountered any bugs.

---

Make sure to customize the README with any additional details specific to your application, such as setup instructions for environment variables, and replace placeholder text with actual information where necessary.
