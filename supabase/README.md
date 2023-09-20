# Migrate database

## 1. Run diff 
```bash
supabase db diff --use-migra -f initial_schema
```

## 2. Run login
```bash
supabase login
```

Use `SUPABASE_ACCESS_TOKEN` from .env

## 3. Run link
```bash
supabase link --project-ref $SUPABASE_PROJECT_REF
```

## 4. Run push
```bash
supabase db push -p $SUPABASE_DB_PASSWORD
```