#!/bin/bash

set -e

DATABASE_URL="postgresql://postgres:yzrhKiriXKrSYAdxIdPSjNuNseQkhjAe@postgres.railway.internal:5432/railway"

# Run Prisma Migrations
echo "Running Prisma Migrations..."
npx prisma migrate deploy --url "$DATABASE_URL"

# Generate Prisma Client
echo "Generating Prisma Client..."
npx prisma generate --url "$DATABASE_URL"

# Start Uvicorn server
echo "Starting Uvicorn server..."
uvicorn main:app --host 0.0.0.0 --port 3000
