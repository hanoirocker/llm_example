from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PromptSerializer
from transformers import pipeline

# Load the language model from Hugging Face

nlp_pipeline = pipeline("text-generation", model="distilgpt2")

class GenerateTextView(APIView):
    def post(self, request):
        serializer = PromptSerializer(data=request.data)
        if serializer.is_valid():
            prompt = serializer.validated_data["prompt"]
            response = nlp_pipeline(prompt, max_length=100)
            return Response({"response": response[0]['generated_text']}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)