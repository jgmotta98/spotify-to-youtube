# APIs Configuration

## Spotify API

### Setting up the Spotify Developer Account

1. Go to https://develope.spotify.com/dashboard
2. Click on **Create app**
3. Provide an **App name**, an **App description**, use `http://127.0.0.1:3000` on the **Redirect URIs** and pick **Web API**
4. Click **Save**

### Getting the **Cliend ID** and the **Client Secret**

Open the app on the Spotify Developer Dashboard and copy the values from the **Cliend ID** and the **Client Secret** fields under **Basic Information**.

---

## Youtube API

### Setting up the Youtube Data API v3

1. Go to https://console.cloud.google.com/ and log with your **Youtube account**
2. Click on **Select a Project**, then click **New Project**
3. Provide a **Project Name** and **Create**
4. Select the newly created project and search for **Youtube Data API v3** in the search bar
5. Click **Enable** to enable the API.
6. When prompted with `"To use this API, you may need credentials."`, click **Create credentials**
7. Choose **User data**, then click **Next**
8. Enter an **App name**, and **Contact Email(s)** then click **Save and Continue**
9. Click **Save and Continue** on the Scopes (Optional)
10. Select **Desktop App** for the **Application type**, then click **Create**.
11. **Download the credentials** and save the file as `client_secret.json` in the [src](./src/) directory.

### Allow emails on development

To use your YouTube account as the playlist creator, you must grant permission by adding the email as the target audience.

1. Click on the **OAuth consent screen** tab
2. Click on the **Audience** tab
3. Find the **Test users** topic, then click on the `+ Add users`
4. Write and save your **Youtube email**

## Running the code

After all those configurations, you can run the `main.py` file and log in to your YouTube account.

> Please note that the YouTube API has a daily limit of 10,000 units, with each API request consuming 100 units.