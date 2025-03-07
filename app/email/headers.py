"""Email headers"""
MESSAGE_ID = "Message-ID"
IN_REPLY_TO = "In-Reply-To"
REFERENCES = "References"
DATE = "date"
SUBJECT = "Subject"
FROM = "From"
TO = "To"
CONTENT_TYPE = "Content-Type"
CONTENT_DISPOSITION = "Content-Disposition"
CONTENT_TRANSFER_ENCODING = "Content-Transfer-Encoding"
MIME_VERSION = "Mime-Version"
REPLY_TO = "Reply-To"
RECEIVED = "Received"
CC = "Cc"
DKIM_SIGNATURE = "DKIM-Signature"
X_SPAM_STATUS = "X-Spam-Status"

# headers used to DKIM sign in order of preference
DKIM_HEADERS = [
    [MESSAGE_ID.encode(), DATE.encode(), SUBJECT.encode(), FROM.encode(), TO.encode()],
    [FROM.encode(), TO.encode()],
    [MESSAGE_ID.encode(), DATE.encode()],
    [FROM.encode()],
]

SL_DIRECTION = "X-SimpleLogin-Type"
SL_EMAIL_LOG_ID = "X-SimpleLogin-EmailLog-ID"
SL_ENVELOPE_FROM = "X-SimpleLogin-Envelope-From"
SL_ENVELOPE_TO = "X-SimpleLogin-Envelope-To"

MIME_HEADERS = [
    MIME_VERSION,
    CONTENT_TYPE,
    CONTENT_DISPOSITION,
    CONTENT_TRANSFER_ENCODING,
]
# convert to lowercase to facilitate header look up
MIME_HEADERS = [h.lower() for h in MIME_HEADERS]
