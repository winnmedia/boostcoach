#!/bin/bash

set -e

export DATABASE_URL="postgresql://postgres:yzrhKiriXKrSYAdxIdPSjNuNseQkhjAe@postgres.railway.internal:5432/railway"

# Run Prisma Migrations
echo "Running Prisma Migrations..."
npx prisma migrate deploy

# Generate Prisma Client
echo "Generating Prisma Client..."
npx prisma generate || { echo "Error: Prisma Client generation failed!"; exit 1; }

# Start Uvicorn server
echo "Starting Uvicorn server..."
uvicorn main:app --host 0.0.0.0 --port 3000
