import json
import urllib.request

def lambda_handler(event, context):
    """
    Downloads a text file from a URL and returns word statistics
    """
    try:
        # Get URL from event
        url = event.get('url')

        if not url:
            return {
                'statusCode': 400,
                'body': json.dumps({'error': 'Missing url parameter'})
            }

        # Download content from URL
        with urllib.request.urlopen(url, timeout=10) as response:
            text = response.read().decode('utf-8')

        # Calculate statistics
        word_count = len(text.split())
        char_count = len(text)
        char_count_no_spaces = len(text.replace(' ', ''))
        line_count = len(text.splitlines())

        # Count vowels
        vowels = 'aeiouAEIOU'
        vowel_count = sum(1 for char in text if char in vowels)

        result = {
            'url': url,
            'word_count': word_count,
            'character_count': char_count,
            'character_count_no_spaces': char_count_no_spaces,
            'line_count': line_count,
            'vowel_count': vowel_count
        }

        return {
            'statusCode': 200,
            'body': json.dumps(result)
        }

    except urllib.error.HTTPError as e:
        return {
            'statusCode': e.code,
            'body': json.dumps({'error': f'HTTP Error: {e.code} - {e.reason}'})
        }
    except urllib.error.URLError as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': f'URL Error: {str(e.reason)}'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
