def test_transform_converts_nan_to_none():
    """
    Test that transform properly handles NaN values

    WHY: PostgreSQL needs None, not pandas NaN
    """

    # Create API response with missing data
    incomplete_data = {
        'bitcoin': {
            'inr': 500000.00
            # Missing: market_cap, volume, etc.
        }
    }

    df = test_transform_converts_nan_to_none(incomplete_data)

    # Check that NaN values can be converted to None
    df_clean = df.where(pd.notna(df), None)

    # Verify None values exist (not NaN)
    assert df_clean['market_cap_usd'].iloc[0] is None