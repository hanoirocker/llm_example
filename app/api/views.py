from django.core.cache import cache
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PromptSerializer
from transformers import pipeline

# Load the language model from Hugging Face

nlp_pipeline = pipeline("text-generation", model="facebook/opt-1.3b")

class GenerateTextView(APIView):
    def post(self, request):
        serializer = PromptSerializer(data=request.data)
        if serializer.is_valid():
            prompt = serializer.validated_data["prompt"]

            # Check if the prompt is already in the cache
            cached_response = cache.get(prompt)
            if cached_response:
                return Response({"response": cached_response, "cached": True}, status=status.HTTP_200_OK)

            # If prompt is not in the cache, generate the text
            response = nlp_pipeline(prompt, max_length=100, num_return_sequences=1,
                                    repetition_penalty=1.2, temperature=0.7)
            
            generated_text = response[0]['generated_text'].replace(prompt, "").strip()

            # cache the generated text
            cache.set(prompt, generated_text, timeout=3600)
            
            return Response({"response": generated_text}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)