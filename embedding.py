from langchain_ollama import OllamaEmbeddings
# from langchain_aws import BedrockEmbeddings


#to use the same embedding function throughout the code
def get_embedding_function():

    # # #create embedding for each chunk - key for the database
    # embeddings = BedrockEmbeddings(
    #     credentials_profile_name="default", region_name="us-east-1"
    # )
    embeddings = OllamaEmbeddings(model="mistral")
    return embeddings