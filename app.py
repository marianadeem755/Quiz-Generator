import streamlit as st
import random
import streamlit as st
import random
import streamlit as st
import random
import time
# Sample questions for each category
questions = {
    "Python Basics": [
        {"question": "What is the output of print(type([]))?", "options": ["<class 'list'>", "<class 'dict'>", "<class 'tuple'>"], "answer": "<class 'list'>"},
        {"question": "What keyword is used to define a function in Python?", "options": ["def", "function", "fun"], "answer": "def"},
        {"question": "How do you create a list in Python?", "options": ["[]", "{}", "()"], "answer": "[]"},
        {"question": "What method adds an element to the end of a list?", "options": ["append()", "add()", "insert()"], "answer": "append()"},
        {"question": "What is the purpose of the self keyword in class methods?", "options": ["To refer to the instance", "To refer to the class", "To define a function"], "answer": "To refer to the instance"},
        {"question": "How can you handle exceptions in Python?", "options": ["try/except", "catch", "throw"], "answer": "try/except"},
        {"question": "What is the difference between == and is?", "options": ["Value vs Identity", "Type vs Value", "None"], "answer": "Value vs Identity"},
        {"question": "How do you read a file in Python?", "options": ["open()", "read()", "file()"], "answer": "open()"},
        {"question": "What does the len() function do?", "options": ["Returns the length", "Returns the type", "Returns the sum"], "answer": "Returns the length"},
        {"question": "How can you convert a string to an integer?", "options": ["int()", "str()", "float()"], "answer": "int()"},
        {"question": "What is a lambda function?", "options": ["Anonymous function", "A type of loop", "None"], "answer": "Anonymous function"},
        {"question": "How do you create a dictionary in Python?", "options": ["{}", "[]", "()"], "answer": "{}"},
        {"question": "What is list comprehension?", "options": ["Creating lists from existing lists", "Creating dictionaries", "None"], "answer": "Creating lists from existing lists"},
        {"question": "What does the map() function do?", "options": ["Applies a function to all items", "Filters items", "None"], "answer": "Applies a function to all items"},
        {"question": "How can you remove duplicates from a list?", "options": ["set()", "unique()", "distinct()"], "answer": "set()"},
        {"question": "What is the purpose of the with statement?", "options": ["Resource management", "Looping", "Condition checking"], "answer": "Resource management"},
        {"question": "How do you merge two dictionaries in Python?", "options": ["dict.update()", "dict.merge()", "dict.concat()"], "answer": "dict.update()"},
        {"question": "What is the difference between a list and a tuple?", "options": ["Mutability", "Size", "Type"], "answer": "Mutability"},
        {"question": "How do you iterate over a dictionary?", "options": ["for key in dict", "for dict in key", "for item in dict"], "answer": "for key in dict"},
        {"question": "What is the purpose of the enumerate() function?", "options": ["To get index and value", "To filter lists", "None"], "answer": "To get index and value"},
        {"question": "How can you reverse a list?", "options": ["list.reverse()", "list[::-1]", "None"], "answer": "list.reverse()"},
        {"question": "What is a generator in Python?", "options": ["An iterable", "A function", "Both"], "answer": "Both"},
        {"question": "How do you define a class in Python?", "options": ["class ClassName:", "def ClassName:", "create ClassName:"], "answer": "class ClassName:"},
        {"question": "What is the output of print('Hello' * 3)?", "options": ["HelloHelloHello", "3Hello", "Hello 3"], "answer": "HelloHelloHello"},
        {"question": "How do you check if a key exists in a dictionary?", "options": ["key in dict", "dict.has_key()", "None"], "answer": "key in dict"},
        {"question": "What is the difference between deep copy and shallow copy?", "options": ["Copy level", "Type of data", "None"], "answer": "Copy level"},
        {"question": "How do you sort a list in Python?", "options": ["list.sort()", "sorted(list)", "Both"], "answer": "Both"},
        {"question": "What is the purpose of the __init__ method?", "options": ["Constructor", "Destructor", "None"], "answer": "Constructor"},
        {"question": "How can you concatenate two strings?", "options": ["str1 + str2", "str1.concat(str2)", "None"], "answer": "str1 + str2"},
        {"question": "What is the output of print(bool(''))?", "options": ["False", "True", "None"], "answer": "False"},
        {"question": "What is the output of print(type({}))?", "options": ["<class 'dict'>", "<class 'list'>", "<class 'tuple'>"], "answer": "<class 'dict'>"},
        {"question": "What is the output of print(type(()))?", "options": ["<class 'tuple'>", "<class 'list'>", "<class 'dict'>"], "answer": "<class 'tuple'>"},
        {"question": "What is a decorator in Python?", "options": ["A function that wraps another function", "A type of class", "None"], "answer": "A function that wraps another function"},
        {"question": "How do you create a virtual environment?", "options": ["python -m venv env", "venv create env", "env create"], "answer": "python -m venv env"},
        {"question": "What is the purpose of the global keyword?", "options": ["To access global variables", "To create global variables", "None"], "answer": "To access global variables"},
        {"question": "How can you iterate through a list with index?", "options": ["for i, value in enumerate(list)", "for i in range(len(list))", "None"], "answer": "for i, value in enumerate(list)"},
        {"question": "What is the output of print('Hello'.upper())?", "options": ["HELLO", "Hello", "hello"], "answer": "HELLO"},
        {"question": "How do you remove an item from a list by value?", "options": ["list.remove(value)", "list.pop(value)", "None"], "answer": "list.remove(value)"},
        {"question": "What does the zip() function do?", "options": ["Combines lists", "Filters lists", "None"], "answer": "Combines lists"},
        {"question": "What is the purpose of the assert statement?", "options": ["To check conditions", "To display output", "None"], "answer": "To check conditions"},
        {"question": "How do you create a set in Python?", "options": ["set()", "{}", "Both"], "answer": "Both"},
        {"question": "What is the difference between append() and extend()?", "options": ["Adding single vs multiple items", "Type of item added", "None"], "answer": "Adding single vs multiple items"},
        {"question": "What is a docstring?", "options": ["Documentation string", "Error message", "None"], "answer": "Documentation string"},
        {"question": "How do you sort a dictionary by value?", "options": ["sorted(dict.items())", "dict.sort()", "None"], "answer": "sorted(dict.items())"},
        {"question": "What is the purpose of the pass statement?", "options": ["Placeholder for future code", "To exit a loop", "None"], "answer": "Placeholder for future code"},
        {"question": "What is the use of the in keyword?", "options": ["To check membership", "To iterate", "None"], "answer": "To check membership"},
        {"question": "What is the output of print(bool([]))?", "options": ["False", "True", "None"], "answer": "False"},
        {"question": "How do you copy a list in Python?", "options": ["list.copy()", "list[:] or list.copy()", "None"], "answer": "list[:] or list.copy()"},
        {"question": "What is the output of print(3 == 3.0)?", "options": ["True", "False", "None"], "answer": "True"},
    ],
    "Data Science": [
        {"question": "What is the purpose of data normalization?", "options": ["To scale data", "To clean data", "None"], "answer": "To scale data"},
        {"question": "What does EDA stand for?", "options": ["Exploratory Data Analysis", "Effective Data Analytics", "None"], "answer": "Exploratory Data Analysis"},
        {"question": "What library is commonly used for data manipulation in Python?", "options": ["NumPy", "Pandas", "Matplotlib"], "answer": "Pandas"},
        {"question": "What is the difference between supervised and unsupervised learning?", "options": ["Labeled vs Unlabeled data", "Type of algorithms", "None"], "answer": "Labeled vs Unlabeled data"},
        {"question": "What is a confusion matrix used for?", "options": ["Evaluating classification models", "Data visualization", "None"], "answer": "Evaluating classification models"},
        {"question": "What is overfitting?", "options": ["Model learns noise", "Underfitting", "None"], "answer": "Model learns noise"},
        {"question": "How can you handle missing values in a dataset?", "options": ["Drop, fill, or interpolate", "Ignore", "None"], "answer": "Drop, fill, or interpolate"},
        {"question": "What does PCA stand for?", "options": ["Principal Component Analysis", "Partial Correlation Analysis", "None"], "answer": "Principal Component Analysis"},
        {"question": "What is the purpose of feature scaling?", "options": ["To normalize data", "To reduce dimensionality", "None"], "answer": "To normalize data"},
        {"question": "What is a scatter plot used for?", "options": ["Showing relationships", "Data distribution", "None"], "answer": "Showing relationships"},
        {"question": "What is the difference between classification and regression?", "options": ["Categorical vs Continuous", "Type of output", "None"], "answer": "Categorical vs Continuous"},
        {"question": "What library is used for data visualization in Python?", "options": ["Matplotlib", "Pandas", "NumPy"], "answer": "Matplotlib"},
        {"question": "What does 'AI' stand for?", "options": ["Artificial Intelligence", "Automated Interface", "Applied Informatics"], "answer": "Artificial Intelligence"},
        {"question": "What is a hypothesis test?", "options": ["Statistical test", "Data cleaning method", "None"], "answer": "Statistical test"},
        {"question": "What is the purpose of cross-validation?", "options": ["Model evaluation", "Data cleaning", "None"], "answer": "Model evaluation"},
        {"question": "What is a time series analysis?", "options": ["Analyzing data over time", "Data distribution", "None"], "answer": "Analyzing data over time"},
        {"question": "What does the term 'bias' refer to in machine learning?", "options": ["Error due to assumptions", "Data imbalance", "Both"], "answer": "Both"},
        {"question": "What is a decision tree?", "options": ["Model for classification", "Data visualization", "None"], "answer": "Model for classification"},
        {"question": "What is the purpose of the K-means algorithm?", "options": ["Clustering", "Classification", "None"], "answer": "Clustering"},
        {"question": "What is A/B testing?", "options": ["Comparing two versions", "Data cleaning", "None"], "answer": "Comparing two versions"},
        {"question": "What does the term 'outlier' mean?", "options": ["An extreme value", "Average value", "None"], "answer": "An extreme value"},
        {"question": "How can you determine the correlation between two variables?", "options": ["Using correlation coefficient", "Visual inspection", "None"], "answer": "Using correlation coefficient"},
        {"question": "What is the significance of the ROC curve?", "options": ["Evaluating classifiers", "Data visualization", "None"], "answer": "Evaluating classifiers"},
        {"question": "What is a categorical variable?", "options": ["Qualitative variable", "Quantitative variable", "None"], "answer": "Qualitative variable"},
        {"question": "What is the role of a data engineer?", "options": ["Data pipeline construction", "Data analysis", "None"], "answer": "Data pipeline construction"},
        {"question": "How do you evaluate a machine learning model?", "options": ["Using metrics", "Visual inspection", "None"], "answer": "Using metrics"},
        {"question": "What is the purpose of feature engineering?", "options": ["Improving model performance", "Data cleaning", "None"], "answer": "Improving model performance"},
        {"question": "What is a linear regression model?", "options": ["Predicts continuous values", "Classifies data", "None"], "answer": "Predicts continuous values"},
        {"question": "What are the assumptions of linear regression?", "options": ["Linearity, independence", "Normality, homoscedasticity", "Both"], "answer": "Both"},
        {"question": "What does the term 'ensemble learning' mean?", "options": ["Combining multiple models", "Single model", "None"], "answer": "Combining multiple models"},
        {"question": "What is a random forest?", "options": ["Ensemble of decision trees", "Single decision tree", "None"], "answer": "Ensemble of decision trees"},
        {"question": "What is the purpose of data visualization?", "options": ["To convey information", "To clean data", "None"], "answer": "To convey information"},
        {"question": "What is the difference between classification and clustering?", "options": ["Labeled vs Unlabeled data", "Model type", "None"], "answer": "Labeled vs Unlabeled data"},
        {"question": "What does an F1 score measure?", "options": ["Model accuracy", "Balance between precision and recall", "None"], "answer": "Balance between precision and recall"},
        {"question": "What is feature selection?", "options": ["Choosing important features", "Data cleaning", "None"], "answer": "Choosing important features"},
        {"question": "What is the purpose of clustering?", "options": ["Grouping similar items", "Data cleaning", "None"], "answer": "Grouping similar items"},
        {"question": "What is k-fold cross-validation?", "options": ["Dividing data into k subsets", "Data cleaning", "None"], "answer": "Dividing data into k subsets"},
        {"question": "What is the output of linear regression?", "options": ["A line", "A decision tree", "None"], "answer": "A line"},
    ],
    
    "Generative AI": [
        {"question": "What is the primary function of Generative AI models?", "options": ["To generate new data", "To classify data", "To clean data"], "answer": "To generate new data"},
        {"question": "What does GAN stand for in the context of Generative AI?", "options": ["Generative Adversarial Network", "Generalized Automated Network", "None"], "answer": "Generative Adversarial Network"},
        {"question": "What is the role of a generator and discriminator in GANs?", "options": ["Generator creates data, Discriminator evaluates it", "Generator evaluates data, Discriminator creates it", "None"], "answer": "Generator creates data, Discriminator evaluates it"},
        {"question": "How does a Variational Autoencoder (VAE) differ from a GAN?", "options": ["VAE generates data probabilistically", "GAN uses a single model", "None"], "answer": "VAE generates data probabilistically"},
        {"question": "What is the purpose of a Latent Space in a Generative model?", "options": ["To represent data in a compressed form", "To clean data", "None"], "answer": "To represent data in a compressed form"},
        {"question": "How does a Transformer architecture contribute to Generative AI?", "options": ["By processing sequential data", "By generating images", "None"], "answer": "By processing sequential data"},
        {"question": "What is a Markov Chain Monte Carlo (MCMC) used for in Generative AI?", "options": ["For generating synthetic data", "For data clustering", "None"], "answer": "For generating synthetic data"},
        {"question": "How does a text-to-image Generative model work?", "options": ["By converting textual descriptions to visual content", "By using data augmentation", "None"], "answer": "By converting textual descriptions to visual content"},
        {"question": "What are some real-world applications of Generative AI in creative industries?", "options": ["Art generation", "Music composition", "Both"], "answer": "Both"},
        {"question": "What is the significance of the attention mechanism in Generative AI models?", "options": ["It helps the model focus on relevant parts of data", "It improves data cleaning", "None"], "answer": "It helps the model focus on relevant parts of data"},
        {"question": "What are the ethical concerns associated with Generative AI?", "options": ["Deepfakes", "Copyright infringement", "Both"], "answer": "Both"},
        {"question": "How can Generative AI be used in content creation (e.g., art, music, and writing)?", "options": ["By generating new works based on patterns", "By analyzing existing content", "None"], "answer": "By generating new works based on patterns"},
        {"question": "What is the role of reinforcement learning in Generative AI models?", "options": ["It helps the model learn from feedback", "It improves data scaling", "None"], "answer": "It helps the model learn from feedback"},
        {"question": "What are the challenges in training large-scale Generative AI models?", "options": ["Computational resources", "Model complexity", "Both"], "answer": "Both"},
        {"question": "How does GPT (Generative Pretrained Transformer) function in text generation?", "options": ["By using pre-trained knowledge", "By using data from the web", "None"], "answer": "By using pre-trained knowledge"},
        {"question": "What is the significance of unsupervised learning in the context of Generative AI?", "options": ["It allows for learning without labeled data", "It requires labeled data", "None"], "answer": "It allows for learning without labeled data"},
        {"question": "What are some risks of deepfake generation in Generative AI?", "options": ["Misinformation", "Privacy invasion", "Both"], "answer": "Both"},
        {"question": "How does a Diffusion Model in Generative AI generate images?", "options": ["By iteratively refining images", "By using neural networks", "None"], "answer": "By iteratively refining images"},
        {"question": "What is the difference between a Generative model and a Discriminative model?", "options": ["Generative models generate data", "Discriminative models generate data", "None"], "answer": "Generative models generate data"},
        {"question": "What are the key differences between GANs and VAEs in generating images?", "options": ["GANs use adversarial networks, VAEs use probabilistic modeling", "GANs and VAEs are identical", "None"], "answer": "GANs use adversarial networks, VAEs use probabilistic modeling"},
        {"question": "How do generative models contribute to data augmentation in machine learning?", "options": ["By creating new synthetic data", "By labeling data", "None"], "answer": "By creating new synthetic data"},
        {"question": "What are some limitations of Generative AI in text generation?", "options": ["Lack of Human Contextual Understanding", "Overfitting", "None"], "answer": "Lack of Human Contextual Understanding"},
        {"question": "How can Generative AI be applied in drug discovery and biology?", "options": ["By predicting molecular structures", "By generating new drugs", "None"], "answer": "By predicting molecular structures"},
        {"question": "What is the concept of \"sampling\" in the context of Generative AI?", "options": ["Selecting data points to generate new samples", "Cleaning data", "None"], "answer": "Selecting data points to generate new samples"},
        {"question": "How does reinforcement learning improve the performance of generative models?", "options": ["By encouraging exploration", "By reducing data bias", "None"], "answer": "By encouraging exploration"},
        {"question": "What are the applications of GANs in computer vision?", "options": ["Image generation", "Image enhancement", "Both"], "answer": "Both"},
        {"question": "How do large pre-trained models like GPT-3 enable text generation?", "options": ["By leveraging vast amounts of data", "By using unsupervised learning", "None"], "answer": "By leveraging vast amounts of data"},
        {"question": "What role do neural networks play in Generative AI?", "options": ["They model complex data relationships", "They clean data", "None"], "answer": "They model complex data relationships"},
        {"question": "What are some challenges in ensuring diversity in generated outputs by Generative AI?", "options": ["Mode collapse", "Lack of Human Contextual Understanding", "Both"], "answer": "Both"},
        {"question": "How does Conditional Generative AI work in generating targeted outputs?", "options": ["By conditioning on specific inputs", "By using unsupervised learning", "None"], "answer": "By conditioning on specific inputs"},
        {"question": "What is the difference between a Generative AI model and a regular neural network?", "options": ["Generative AI models create data", "Both are the same", "None"], "answer": "Generative AI models create data"},
        {"question": "What is the concept of “mode collapse” in GANs?", "options": ["Generator produces limited outputs", "Discriminator fails to identify fake data", "None"], "answer": "Generator produces limited outputs"},
        {"question": "What are some tools used to evaluate the performance of a Generative AI model?", "options": ["Inception Score", "Fréchet Inception Distance", "Both"], "answer": "Both"},
        {"question": "How can Generative AI assist in designing new architectures or solutions?", "options": ["By proposing new designs based on data patterns", "By cleaning data", "None"], "answer": "By proposing new designs based on data patterns"},
        {"question": "How does text-to-speech generation work in Generative AI models?", "options": ["By converting text to audible speech", "By generating text-based content", "None"], "answer": "By converting text to audible speech"},
        {"question": "What are the implications of Generative AI for intellectual property and copyright?", "options": ["Copyright ownership of generated content", "Unclear legal framework", "Both"], "answer": "Both"},
        {"question": "How can Generative AI models be used to create synthetic data for training?", "options": ["By generating new data similar to real data", "By cleaning existing data", "None"], "answer": "By generating new data similar to real data"},
        {"question": "What is the role of the \"latent vector\" in Generative AI models like GANs?", "options": ["It represents the compressed input data", "It generates random noise", "None"], "answer": "It represents the compressed input data"},
        {"question": "What is the role of fine-tuning in generative models like GPT-3?", "options": ["It helps adapt the model to specific tasks", "It increases model size", "None"], "answer": "It helps adapt the model to specific tasks"},
        {"question": "How does transfer learning enhance the capabilities of Generative AI models?", "options": ["By leveraging pre-trained knowledge", "By increasing model complexity", "None"], "answer": "By leveraging pre-trained knowledge"}
    ],
    
    "Agentic AI": [
        {"question": "What does the term “Agentic AI” refer to?", "options": ["AI with autonomous decision-making capabilities", "AI for data classification", "None"], "answer": "AI with autonomous decision-making capabilities"},
        {"question": "How do autonomous agents interact with their environment in Agentic AI?", "options": ["By perceiving and acting based on feedback", "By collecting data", "None"], "answer": "By perceiving and acting based on feedback"},
        {"question": "What is the key difference between reactive AI and Agentic AI?", "options": ["Agentic AI makes autonomous decisions", "Reactive AI makes autonomous decisions", "None"], "answer": "Agentic AI makes autonomous decisions"},
        {"question": "How does decision-making occur in Agentic AI systems?", "options": ["Based on feedback and goal optimization", "By following pre-defined rules", "None"], "answer": "Based on feedback and goal optimization"},
        {"question": "What is reinforcement learning, and how is it used in Agentic AI?", "options": ["A learning method based on rewards and penalties", "A supervised learning technique", "None"], "answer": "A learning method based on rewards and penalties"},
        {"question": "How do Agentic AI systems handle multi-agent environments?", "options": ["By collaborating or competing with other agents", "By acting independently", "None"], "answer": "By collaborating or competing with other agents"},
        {"question": "What is the concept of a reward signal in Agentic AI?", "options": ["A feedback used to guide decision-making", "A measure of performance", "None"], "answer": "A feedback used to guide decision-making"},
        {"question": "What is the role of exploration and exploitation in Agentic AI?", "options": ["Exploration seeks new knowledge, Exploitation maximizes reward", "Both are the same", "None"], "answer": "Exploration seeks new knowledge, Exploitation maximizes reward"},
        {"question": "How does the concept of bounded rationality apply to Agentic AI?", "options": ["AI agents make optimal decisions within limits", "AI agents always make the best decisions", "None"], "answer": "AI agents make optimal decisions within limits"},
        {"question": "How do Agentic AI systems optimize their actions to achieve long-term goals?", "options": ["By evaluating actions over time", "By following fixed rules", "None"], "answer": "By evaluating actions over time"},
        {"question": "What challenges do Agentic AI systems face when dealing with ambiguity or uncertainty?", "options": ["Limited information and unpredictable outcomes", "Too much data", "None"], "answer": "Limited information and unpredictable outcomes"},
        {"question": "How do ethics and responsibility play a role in the design of Agentic AI?", "options": ["Ensuring AI decisions align with human values", "Reducing computational resources", "None"], "answer": "Ensuring AI decisions align with human values"},
        {"question": "What is the difference between deliberative and reactive decision-making in Agentic AI?", "options": ["Deliberative involves planning, Reactive involves immediate responses", "Both are the same", "None"], "answer": "Deliberative involves planning, Reactive involves immediate responses"},
        {"question": "What is the concept of “autonomy” in Agentic AI systems?", "options": ["Ability to make independent decisions", "Ability to collect data", "None"], "answer": "Ability to make independent decisions"},
        {"question": "How does reward shaping affect the behavior of Agentic AI?", "options": ["It modifies the reward signal to guide behavior", "It removes negative rewards", "None"], "answer": "It modifies the reward signal to guide behavior"},
        {"question": "What are some key examples of Agentic AI in real-world applications?", "options": ["Autonomous vehicles", "Chatbots", "Both"], "answer": "Both"},
        {"question": "How can Agentic AI systems learn from past experiences to improve future decisions?", "options": ["Through reinforcement learning", "By observing human actions", "None"], "answer": "Through reinforcement learning"},
        {"question": "What are some of the safety concerns with fully autonomous Agentic AI?", "options": ["Unintended actions", "Lack of Human Oversight", "Both"], "answer": "Both"},
        {"question": "What techniques are used to prevent agent misbehavior in Agentic AI systems?", "options": ["Constraints, monitoring, and reward adjustments", "None", "Both"], "answer": "Constraints, monitoring, and reward adjustments"}
    ]
    }
def main():
    st.set_page_config(page_title="Smart Quiz Generator", page_icon="🧠", layout="centered")

    st.markdown("""
    <style>
        /* Main Content Area Background */
        .stApp {
            background-image: url('https://images.rawpixel.com/image_800/czNmcy1wcml2YXRlL3Jhd3BpeGVsX2ltYWdlcy93ZWJzaXRlX2NvbnRlbnQvbHIvcm0yODEtYWRqLTA1NC1qb2I1OTguanBn.jpg');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            min-height: 100vh;
            color: darkred;
        }

        /* Sidebar Background */
        section[data-testid="stSidebar"] {
            background-image: url('https://img.freepik.com/premium-photo/hand-drawn-abstract-background-design_481527-40048.jpg');
            background-size: cover;
            background-position: center;
        }
    </style>
    """, unsafe_allow_html=True)
    # Sidebar Profile Links
    st.sidebar.markdown("## 🎉Author: Maria Nadeem🌟")
    st.sidebar.markdown("## 🔗 Connect With Me")
    st.sidebar.markdown("""
    <div>
        <a href="https://github.com/marianadeem755" target="_blank">
            <img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" width="30px"> GitHub
        </a><br><br>
        <a href="https://www.kaggle.com/marianadeem755" target="_blank">
            <img src="https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/189_Kaggle_logo_logos-512.png" width="30px"> Kaggle
        </a><br><br>
        <a href="mailto:marianadeem755@gmail.com">
            <img src="https://cdn-icons-png.flaticon.com/512/561/561127.png" width="30px"> Email
        </a><br><br>
        <a href="https://huggingface.co/maria355" target="_blank">
            <img src="https://huggingface.co/front/assets/huggingface_logo-noborder.svg" width="30px"> Hugging Face
        </a>
    </div>
    """, unsafe_allow_html=True)

    # Sidebar domain selection
    st.sidebar.markdown("## 🎯 Choose a Focus Area")
    selected_domain = st.sidebar.selectbox("Select your Expertise", list(questions.keys()))

    st.title("🧠 Quiz Generator")

    # Initialize session state
    if 'quiz_started' not in st.session_state:
        st.session_state.quiz_started = False
    if 'current_question_index' not in st.session_state:
        st.session_state.current_question_index = 0
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'selected_category' not in st.session_state:
        st.session_state.selected_category = None
    if 'answered' not in st.session_state:
        st.session_state.answered = False
    if 'user_answer' not in st.session_state:
        st.session_state.user_answer = None
    if 'quiz_questions' not in st.session_state:
        st.session_state.quiz_questions = []
    if 'start_time' not in st.session_state:
        st.session_state.start_time = None

    if not st.session_state.quiz_started:
        st.subheader("Get ready to test your knowledge! 🎯")
        if st.button("Start Quiz"):
            st.session_state.quiz_started = True
            st.session_state.selected_category = selected_domain
            st.session_state.quiz_questions = random.sample(
                questions[selected_domain], 
                min(30, len(questions[selected_domain]))
            )
            st.session_state.current_question_index = 0
            st.session_state.score = 0
            st.session_state.start_time = time.time()
            st.rerun()

    else:
        # Display current question
        if st.session_state.current_question_index < len(st.session_state.quiz_questions):
            current_question = st.session_state.quiz_questions[st.session_state.current_question_index]

            st.subheader(f"Question {st.session_state.current_question_index + 1}")
            st.markdown(f"### {current_question['question']}")

            elapsed_time = time.time() - st.session_state.start_time
            remaining_time = max(60 - int(elapsed_time), 0)

            # Timer display
            progress = st.progress(0)
            progress.progress((60 - remaining_time) / 60)
            time_display = st.empty()
            time_display.markdown(f"⏳ **Time left: {remaining_time} seconds**")

            if not st.session_state.answered:
                user_answer = st.radio(
                    "Select your answer:",
                    current_question['options'],
                    key=f"question_{st.session_state.current_question_index}"
                )

                submit = st.button("Submit Answer ✅")

                if submit:
                    st.session_state.answered = True
                    st.session_state.user_answer = user_answer

                    if user_answer == current_question['answer']:
                        st.session_state.score += 1
                        st.success("✅ Correct Answer!")
                    else:
                        st.error(f"❌ Wrong Answer! Correct: **{current_question['answer']}**")

            # If time's up and not answered yet
            if remaining_time == 0 and not st.session_state.answered:
                st.warning("⏰ Time's up!")
                st.session_state.answered = True
                st.session_state.user_answer = None

            # Only show "Next" button AFTER answered OR timeout
            if st.session_state.answered:
                next_question = st.button("Next Question ➡️")
                if next_question:
                    st.session_state.current_question_index += 1
                    st.session_state.answered = False
                    st.session_state.user_answer = None
                    st.session_state.start_time = time.time()  # reset timer
                    st.rerun()

            # Refresh page every second ONLY if not answered yet
            if not st.session_state.answered and remaining_time > 0:
                time.sleep(1)
                st.experimental_rerun()

        else:
            # Quiz completed
            st.success(f"🏁 Quiz completed! Your final score: {st.session_state.score}/{len(st.session_state.quiz_questions)}")
            st.balloons()

            if st.button("Restart Quiz 🔄"):
                for key in list(st.session_state.keys()):
                    del st.session_state[key]
                st.rerun()

if __name__ == "__main__":
    main()