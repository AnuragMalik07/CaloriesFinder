# AI CaloriesFinder

## Description
AI Calories Finder is a web application built with Streamlit that leverages Google's Gemini Pro Vision model to analyze food items in an uploaded image and calculate their total caloric content. The application also provides a detailed breakdown of each food item's calorie count. This tool is designed to assist nutritionists and health-conscious individuals in quickly estimating the caloric content of meals based on visual input.

## Features
- **Image Upload:** Users can upload images in JPG, JPEG, or PNG formats.
- **AI-Powered Analysis:** Utilizes Google's Generative AI model (Gemini Pro Vision) to identify food items and calculate their calories.
- **Calorie Breakdown:** Provides a detailed list of food items with their respective calorie counts.
- **User-Friendly Interface:** Simple and intuitive interface built with Streamlit.

## Installation
To run the application locally, follow these steps:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/ai-calories-finder.git
    cd ai-calories-finder
    ```

2. **Create and activate a virtual environment in VsCode:**
    ```bash
    conda create venv python=3.10 -y
    conda activate
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up API keys:**
    - Create a `.env` file in the project directory.
    - Add your Google API key to the `.env` file:
      ```
      GOOGLE_API_KEY=your_google_api_key
      ```

5. **Run the application:**
    ```bash
    streamlit run app.py
    ```

## Usage
1. **Upload an Image:** Click on the "Choose image..." button to upload an image of your meal.
2. **Submit for Analysis:** After uploading the image, click the "Tell me the total calories" button.
3. **View Results:** The AI will analyze the image and display the total calories along with a detailed breakdown of each food item and its caloric content.

## Dependencies
- `streamlit`
- `google.generativeai`
- `python-dotenv`

## Contributing
Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or bug fixes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements
- Special thanks to the developers of Streamlit for providing an easy-to-use web framework.
- Thanks to Google for their powerful generative AI model, Gemini Pro Vision.

