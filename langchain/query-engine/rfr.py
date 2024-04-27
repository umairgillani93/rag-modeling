from langchain.embeddings.base import Embeddings
from langchain.vectorstores import Chroma
from langchain.schema import BaseRetriever

class RFR(BaseRetriever):
    '''
    custom class to remove redundant duplicate documents 
    from out retriever search.

    this will depend upon the similarity score.
    we'll query the chromadb and keep only those 
    values that'll have score of 0.8 - 1 for similarity.

    we'll be implementing two mendatory methods for that
    1. get_relevant_documents
    2. async aget_relevant_document

    our custom class will derive from the BaseRetriever
    having all the functions and attributes of parent class.

    last but not least, we're going to require input from user,
    that how they like to calculate the embeddings, or which method
    they want to prefer, as we know there are ton of methods out there.

    '''

    embeddings: Embeddings
    chroma: Chroma

    def get_relevant_documents(self, query):
        '''
        this function does the following things:

        1. calculate the embeddings for passed query.
        2. take the embeddings and feed them into 
           max_marginal_relevance_search_by_vector -> List[DOCUMENTS]
           '''
        emb = self.embeddings.embed_query(query)

        return self.chroma.max_marginal_relevance_search_by_vector(
                emb,
                lambda_mult = 0.8
                )

    async def aget_relevant_documents(self):
        return []
