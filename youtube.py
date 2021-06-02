# -*- coding: utf-8 -*-

# Sample Python code for youtubeAnalytics.reports.query
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python
#https://developers.google.com/youtube/analytics/sample-requxests

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtubeAnalytics"
    api_version = "v2"
    client_secrets_file = "/Users/awssteph/Applications/YOUR_CLIENT_SECRET_FILE.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes)
    credentials = flow.run_console()
    youtube_analytics = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials)

    request = youtube_analytics.reports().query(
        endDate="2021-06-30",
        ids="channel==MINE",
        metrics="views,comments,likes,dislikes,estimatedMinutesWatched,averageViewDuration",
        startDate="2021-05-18"
    )
    response = request.execute()

    print(response)

if __name__ == "__main__":
    main()