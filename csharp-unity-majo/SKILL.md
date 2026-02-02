---
name: csharp-unity-majo
description: C# and Unity development standards for Mark's projects. Use when writing C# code, especially for Unity game development. Covers naming conventions, XML documentation, callback patterns, and Debug.Log formatting.
license: Unlicense OR 0BSD
metadata:
  author: Mark Joshwel <mark@joshwel.co>
  version: "2026.2.2"
---

# C# and Unity Standards (Mark)

Standards for writing C# code, with Unity-specific patterns.

## Naming Conventions

### Field Naming by Access Level

```csharp
public double lightness;           // public: camelCase
protected Slider LightnessSlider;  // protected: PascalCase
private FirebaseAuth _auth;        // private: _camelCase
```

| Access Level | Convention | Example |
|-------------|------------|---------|
| `public` | camelCase | `lightness`, `userData`, `isReady` |
| `protected` | PascalCase | `LightnessSlider`, `UserData` |
| `private` | _camelCase | `_auth`, `_userData`, `_isInitialised` |

### Method Naming

Methods use **PascalCase** regardless of access level:

```csharp
public void CalculateSimilarity() { }
private void _initialiseAuth() { }  // ❌ WRONG
private void InitialiseAuth() { }   // ✅ CORRECT
```

### Preserved External Code

When porting code from external sources, **preserve the original naming** for traceability:

```csharp
// https://bottosson.github.io/posts/oklab/ (public domain)
public static Lab linear_srgb_to_oklab(RGB c)  // snake_case preserved
{
    // implementation...
}
```

Add a comment linking to the original source.

## XML Documentation

Use XML documentation for public APIs:

```csharp
/// <summary>
///     calculate a similarity percentage from a colour distance
/// </summary>
/// <param name="delta">the delta object returned by CalculateDistance</param>
/// <param name="chromaMax">maximum chroma value, defaults to 1.0f</param>
/// <returns>a similarity percentage (0-100)</returns>
public static float CalculateSimilarity(DeltaLabChE delta, float chromaMax = 1.0f)
{
    // implementation...
}
```

Key points:
- Use lowercase in documentation text (sentence case)
- Indent content within `<summary>` tags
- Include `<param>` for all parameters
- Include `<returns>` for non-void methods
- Use British spellings (colour, initialise, behaviour)

## Callback Registration Pattern

Use List-based callback registration for event systems:

```csharp
private readonly List<Action<FirebaseUser>> _onSignInCallbacks = new();

public void RegisterOnSignInCallback(Action<FirebaseUser> callback)
{
    _onSignInCallbacks.Add(callback);
    Debug.Log($"registering OnSignInCallback ({_onSignInCallbacks.Count})");
}

private void FireOnSignInCallbacks()
{
    foreach (var callback in _onSignInCallbacks)
    {
        try
        {
            callback.Invoke(_user);
        }
        catch (Exception e)
        {
            Debug.LogError($"error invoking callback: {e.Message}");
        }
    }
}
```

Pattern elements:
- Private `List<Action<T>>` for storing callbacks
- Public `Register*Callback` method
- Private `Fire*Callbacks` method with try-catch
- Log registration count for debugging

## Debug.Log Formatting

Use lowercase messages consistent with error message format:

```csharp
Debug.Log($"initialising authentication service");
Debug.Log($"registering OnSignInCallback ({_onSignInCallbacks.Count})");
Debug.LogWarning($"user not authenticated, skipping sync");
Debug.LogError($"error invoking callback: {e.Message}");
```

For errors, follow the standard format:
```csharp
Debug.LogError($"authservice: error: failed to sign in: {e.Message}");
```

## British Spellings

Use British spellings in code identifiers and documentation. See `majo-standards` for the complete list.

Common C# examples:
- `Initialise()` not `Initialize()`
- `colour` not `color`
- `behaviour` not `behavior`
- `Serialise()` not `Serialize()`
- `Normalise()` not `Normalize()`

**Exception**: When interfacing with Unity or .NET APIs that use American spellings (e.g., `MonoBehaviour`, `Color`), use the API's spelling for that specific reference.

## Integration

This skill extends `majo-standards`. Always ensure `majo-standards` is loaded for:
- British English spellings
- Error message format
- AGENTS.md maintenance
- Universal code principles

Works alongside:
- `git-majo` — For committing C# changes
- `docs-majo` — For writing C#/Unity documentation
- `task-planning-majo` — For planning Unity projects
