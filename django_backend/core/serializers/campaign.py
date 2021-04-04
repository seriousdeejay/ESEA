from rest_framework import serializers

from ..models import Campaign, EseaAccount, Method, Network

class CampaignSerializer(serializers.ModelSerializer):
    network = serializers.PrimaryKeyRelatedField(queryset=Network.objects.all())
    method = serializers.PrimaryKeyRelatedField(queryset=Method.objects.all())
    class Meta:
        model = Campaign
        fields = ['id', 'name', 'network', 'method', 'organisation_accounts', 'open_survey_date', 'close_survey_date']
        depth = 1

    
    def create(self, validated_data):    
        campaign = Campaign.objects.create(**validated_data)
        for organisation in campaign.network.organisations.all():
            EseaAccount.objects.create(organisation=organisation, method=campaign.method, campaign=campaign)
        return campaign
    
    def update(self, instance, validated_data):
        print('check')
        return instance
