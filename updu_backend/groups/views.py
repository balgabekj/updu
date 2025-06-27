from django.shortcuts import render

# Create your views here.

from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Group
from .serializers import GroupSerializer

class GroupListCreateView(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        group = serializer.save(created_by=self.request.user)
        group.members.add(self.request.user)

class JoinGroupView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            group = Group.objects.get(pk=pk)
            group.members.add(request.user)
            return Response({'detail': 'You joined the group!'})
        except Group.DoesNotExist:
            return Response({'error': 'Group not found'}, status=status.HTTP_404_NOT_FOUND)


class GroupDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        group = serializer.save()
        if self.request.user not in group.members.all():
            group.members.add(self.request.user)

class LeaveGroupView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            group = Group.objects.get(pk=pk)
            if request.user in group.members.all():
                group.members.remove(request.user)
                return Response({'detail': 'You left the group!'})
            else:
                return Response({'error': 'You are not a member of this group'}, status=status.HTTP_400_BAD_REQUEST)
        except Group.DoesNotExist:
            return Response({'error': 'Group not found'}, status=status.HTTP_404_NOT_FOUND)

class GroupMembersView(generics.ListAPIView):
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        group_id = self.kwargs['pk']
        try:
            group = Group.objects.get(pk=group_id)
            return group.members.all()
        except Group.DoesNotExist:
            return Group.objects.none()

class UserGroupsView(generics.ListAPIView):
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return user.joined_groups.all()

class AddGroupMembersView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        try:
            group = Group.objects.get(pk=pk)
            user_ids = request.data.get('user_ids', [])
            if not isinstance(user_ids, list):
                return Response({'error': 'user_ids must be a list'}, status=status.HTTP_400_BAD_REQUEST)
            added_users = []
            for user_id in user_ids:
                try:
                    user = group.members.model.objects.get(pk=user_id)
                    group.members.add(user)
                    added_users.append(user_id)
                except group.members.model.DoesNotExist:
                    continue
            return Response({'detail': 'Members added', 'added_user_ids': added_users})
        except Group.DoesNotExist:
            return Response({'error': 'Group not found'}, status=status.HTTP_404_NOT_FOUND)
        
