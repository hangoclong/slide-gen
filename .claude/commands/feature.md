# Feature Development Workflow Command

Activates the TDD-based feature development workflow defined in `.claude/workflows/feature.yaml`.

## Usage
```
/feature <feature-name> <feature-description> <affected-layers> [component-type]
```

## Parameters
- **feature-name**: Name of the feature (required)
- **feature-description**: Brief description of what the feature does (required)
- **affected-layers**: Comma-separated list of layers affected (domain,application,infrastructure,presentation) (required)
- **component-type**: Type of component (optional, e.g., "form", "table", "modal")

## Examples
```
/feature "User Authentication" "Add login and registration functionality" "domain,application,infrastructure,presentation"
/feature "Course Enrollment" "Allow students to enroll in course offerings" "application,infrastructure,presentation" "form"
/feature "Quiz Grading" "Implement automatic quiz grading logic" "domain,application"
```

## What it does
1. **RED Phase**: Generates comprehensive failing tests following Testing Trophy principles
2. **GREEN Phase**: Implements minimal code to make tests pass
3. **REFACTOR Phase**: Improves code quality and adds documentation

The workflow follows Clean Architecture principles and enforces the project's TDD protocol.