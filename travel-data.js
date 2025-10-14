// ============================================================================
// 🌍 MY TRAVEL DATA - Easy Maintenance File
// ============================================================================
// 
// HOW TO USE:
// 1. To add a new country: Copy an existing entry and modify it
// 2. To remove a country: Delete the entire line
// 3. Save this file and refresh the page - everything updates automatically!
//
// TIPS:
// - Get country flags from: https://emojipedia.org/flags/
// - Get country IDs from: https://en.wikipedia.org/wiki/ISO_3166-1_numeric
// - Or just add name and flag, leave ID empty - it will still work!
// ============================================================================

const myTravelData = {
    
    // 🌏 ASIA
    asia: [
        { name: 'China', flag: '🇨🇳', id: '156' },
        { name: 'Japan', flag: '🇯🇵', id: '392' },
        { name: 'Cambodia', flag: '🇰🇭', id: '116' },
        { name: 'Philippines', flag: '🇵🇭', id: '608' },
        { name: 'Turkey', flag: '🇹🇷', id: '792' }
        // Add more Asian countries here...
    ],
    
    // 🇪🇺 EUROPE
    europe: [
        { name: 'United Kingdom', flag: '🇬🇧', id: '826' },
        { name: 'Germany', flag: '🇩🇪', id: '276' },
        { name: 'France', flag: '🇫🇷', id: '250' },
        { name: 'Spain', flag: '🇪🇸', id: '724' },
        { name: 'Italy', flag: '🇮🇹', id: '380' },
        { name: 'Portugal', flag: '🇵🇹', id: '620' },
        { name: 'Hungary', flag: '🇭🇺', id: '348' },
        { name: 'Austria', flag: '🇦🇹', id: '040' },
        { name: 'Czech Republic', flag: '🇨🇿', id: '203', altNames: ['Czechia'] },
        { name: 'Vatican City', flag: '🇻🇦', id: '336' },
        { name: 'Monaco', flag: '🇲🇨', id: '492' },
        { name: 'Iceland', flag: '🇮🇸', id: '352' }
        // Add more European countries here...
    ],
    
    // 🌎 AMERICAS
    americas: [
        { name: 'United States', flag: '🇺🇸', id: '840', altNames: ['United States of America'] },
        { name: 'Canada', flag: '🇨🇦', id: '124' },
        { name: 'Mexico', flag: '🇲🇽', id: '484' }
        // Add more American countries here...
    ],
    
    // 🌍 AFRICA
    africa: [
        { name: 'Morocco', flag: '🇲🇦', id: '504' }
        // Add more African countries here...
    ],
    
    // 🌏 OCEANIA
    oceania: [
        { name: 'Australia', flag: '🇦🇺', id: '036' }
        // Add more Oceanian countries here...
    ]
};

// ============================================================================
// 📝 QUICK REFERENCE: Common Country IDs
// ============================================================================
// Asia: Thailand (764), Singapore (702), South Korea (410), India (356), 
//       Vietnam (704), Malaysia (458), Indonesia (360)
// Europe: Netherlands (528), Belgium (056), Switzerland (756), Sweden (752),
//         Norway (578), Denmark (208), Poland (616), Greece (300)
// Americas: Brazil (076), Argentina (032), Chile (152), Peru (604), 
//           Colombia (170), Costa Rica (188)
// Africa: Egypt (818), South Africa (710), Kenya (404), Tanzania (834)
// Oceania: New Zealand (554), Fiji (242)
// ============================================================================
