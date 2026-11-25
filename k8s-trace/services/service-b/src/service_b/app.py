from fastapi import FastAPI
from service_b.api import api_router
from contextlib import asynccontextmanager
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

from opentelemetry.sdk.resources import Resource, SERVICE_NAME
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry import trace



@asynccontextmanager
async def lifespan(app: FastAPI):
    resource = Resource.create(attributes={SERVICE_NAME: "service_b"})
    tracer_provider = TracerProvider(resource=resource)
    span_exporter = OTLPSpanExporter(endpoint="http://jaeger:4317", insecure=True)
    span_processor = BatchSpanProcessor(span_exporter=span_exporter)

    tracer_provider.add_span_processor(span_processor=span_processor)
    trace.set_tracer_provider(tracer_provider=tracer_provider)

    HTTPXClientInstrumentor().instrument()
    FastAPIInstrumentor.instrument_app(app=app, tracer_provider=tracer_provider)

    try:
        yield
    finally:
        HTTPXClientInstrumentor().uninstrument()
        FastAPIInstrumentor.uninstrument_app(app=app)
        tracer_provider.shutdown()


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)
