# RedditPrivatizer

A Python script that deletes all comments and/or posts from your Reddit account (older than a specified cutoff, default 3 days) via the Reddit API, for privacy.

## Features

- Deletes your Reddit comments (and optionally posts)
- Deletes only content older than a specified cutoff (default: 3 days)
- Simple to use and customize

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/fbudimir/reddit-privatizer.git
cd RedditPrivatizer
```

### 2. Create a Reddit App

1. Visit https://www.reddit.com/prefs/apps
2. Click "create another app"
3. Choose "script" as the app type
4. Fill in the required fields (use `http://localhost:8080` as the redirect URI, it's just a placeholder)

### 3. Install Dependencies

```bash
pip install praw
```

### 4. Configure the Script

1. Open the script file
2. Enter your Reddit API credentials:
   - `CLIENT_ID`
   - `CLIENT_SECRET`
   - `USERNAME`
   - `PASSWORD`
   - `USER_AGENT` (here you can enter anything you want, for example "My script")

### 5. Set the Cutoff

By default, the script deletes content older than 3 days.

To change this, modify the cutoff line in the script:

```python
cutoff = time.time() - (3 * 24 * 60 * 60)  # 3 days ago
```

Set `cutoff = 0` to delete everything.

## Usage

### Delete Comments
Run the script as-is to delete all your comments older than the cutoff.

### Delete Posts
To also delete your posts, uncomment the relevant section in the script:

```python
# for submission in reddit.redditor(USERNAME).submissions.new(limit=None):
#     if submission.created_utc < cutoff:
#         print(f"Deleting post from {datetime.utcfromtimestamp(submission.created_utc)}: {submission.title[:30]}...")
#         submission.delete()
```

### Run the Script

```bash
python reddit-privatizer.py
```

## Important Notes

- Reddit may rate-limit deletions. If the script stops, simply re-run it to continue.
- **Warning**: Deletions are permanent! Double-check your cutoff and credentials before running the script.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 