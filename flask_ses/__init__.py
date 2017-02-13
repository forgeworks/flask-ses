import boto.ses

from flask import current_app
try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack

class SESMailer(object):

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        pass
    
    def connect(self):
        return boto.ses.connect_to_region(current_app.config['AWS_REGION'],
                                          aws_access_key_id=current_app.config['AWS_ACCESS_KEY_ID'],
                                          aws_secret_access_key=current_app.config['AWS_SECRET_ACCESS_KEY'])

    @property
    def connection(self):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'ses_connection'):
                ctx.ses_connection = self.connect()
            return ctx.ses_connection

    def send(self, subject, body, to_addresses, source=None, **kwargs):
        source = source or current_app.config['SES_SOURCE_EMAIL']
        return self.connection.send_email(source, subject, body, to_addresses, **kwargs)
