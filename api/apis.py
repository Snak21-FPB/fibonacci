from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from . import serializers


class FibonacciAPIView(APIView):
    def fibonacci(self, n:int) -> int:
        """フィボナッチ数列の n 番目を返す
        
        Parameter
        -----
        n: int
            フィボナッチ数列の何番目をとってくるか指定する
        
        Return
        -----
        fib: int
            フィボナッチ数列の n 番目の値
        
        Example
        -----
        >>> fibonacci(1)
        1
        >>> fibonacci(4)
        3
        """
        
        if n == 1:
            return n
        
        fib_prev = 1
        fib = 1
        
        for _ in range(n-2):
            fib_prev, fib = fib, fib + fib_prev
        
        return fib
    
    def get(self, request):
        """GETレスポンス"""
        
        serializer = serializers.FibonacciSerializer(data={"n": request.query_params.get("n")})
        serializer.is_valid(raise_exception=True)
        n = serializer.data["n"]
        fibonacci = self.fibonacci(n)
        return Response({"result": fibonacci}, status=status.HTTP_200_OK)
